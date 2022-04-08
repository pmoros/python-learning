# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from tkinter.filedialog import test
from unittest import TestCase, main
from unittest.mock import patch, Mock

from tests.unit import create_fake_member
from python_learning.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", Gender.MALE)
        self.member.father = Member(1, "Dad", Gender.MALE)
        self.member.mother = Member(1, "Mom", Gender.FEMALE)

    def test_initialization(self):
        # Check instance
        self.assertEqual(isinstance(self.member, Member), True)

        # Check properties
        self.assertEqual(self.member.id_member, 1)
        self.assertEqual(self.member.name, "Zim")
        self.assertEqual(self.member.gender, Gender.MALE)
        self.assertEqual(self.member.spouse, None)
        self.assertEqual(self.member.children, [])

    def test_set_mother(self):
        mother_demo_a = "mother_demo_a"  # Wrong type
        mother_demo_b = Member(2, "MotherDemoB", Gender.MALE)  # Invalid sex
        mother_demo_c = Member(3, "Mom", Gender.FEMALE)

        # Error case
        self.assertRaises(TypeError, self.member.set_mother, mother_demo_a)
        self.assertRaises(ValueError, self.member.set_mother, mother_demo_b)

        # Success case
        self.member.set_mother(mother_demo_c)
        self.assertEqual(self.member.mother.name, "Mom")
        self.assertEqual(self.member.mother.gender, Gender.FEMALE)

    def test_set_father(self):
        father_demo_a = "father_demo_a"  # Wrong type
        father_demo_b = Member(2, "FatherDemoB", Gender.FEMALE)  # Invalid sex
        father_demo_c = Member(3, "Dad", Gender.MALE)

        # Error case
        self.assertRaises(TypeError, self.member.set_father, father_demo_a)
        self.assertRaises(ValueError, self.member.set_father, father_demo_b)

        # Success case
        self.member.set_father(father_demo_c)
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member.father.gender, Gender.MALE)

    def test_set_spouse(self):
        spouse_demo_a = "SpouseA"
        spouse_demo_b = Member(4, "MaleB", Gender.MALE)
        spouse_demo_c = Member(5, "WomanC", Gender.FEMALE)

        # Error case
        self.assertRaises(TypeError, self.member.set_spouse, spouse_demo_a)
        self.assertRaises(ValueError, self.member.set_spouse, spouse_demo_b)

        # Success case
        self.member.set_spouse(spouse_demo_c)
        self.assertNotEqual(self.member.spouse.gender, self.member.gender)

    def test_add_child(self):
        child_demo_a = "ChildA"
        child_demo_b = Member(6, "ChildB", Gender.MALE)

        # Error case
        self.assertRaises(TypeError, self.member.add_child, child_demo_a)
        self.assertRaises(AttributeError, self.member.add_child, child_demo_b)

        # Success case
        member_female = Member(7, "FemaleAux", Gender.FEMALE)
        member_female.set_spouse(self.member)
        member_female.add_child(child_demo_b)
        self.assertEqual(member_female.children.pop(), child_demo_b)

    def test_get_paternal_grandmother(self):
        test_member = Member(1, "Member", Gender.MALE)
        test_member_father = Member(2, "Member", Gender.MALE)
        test_paternal_grandmother = Member(3, "Paternal GrandMother", Gender.FEMALE)

        # Error cases
        self.assertEqual(test_member.get_paternal_grandmother(), None)

        test_member.father = test_member_father
        self.assertEqual(test_member.get_paternal_grandmother(), None)

        # Success case
        test_member_father.mother = test_paternal_grandmother
        self.assertEqual(
            test_member.get_paternal_grandmother(), test_paternal_grandmother
        )

    def test_get_maternal_grandmother(self):
        test_member = Member(1, "Member", Gender.MALE)
        test_member_mother = Member(2, "Member", Gender.MALE)
        test_maternal_grandmother = Member(3, "Maternal GrandMother", Gender.FEMALE)

        # Error cases
        self.assertEqual(test_member.get_maternal_grandmother(), None)

        test_member.mother = test_member_mother
        self.assertEqual(test_member.get_maternal_grandmother(), None)

        # Success case
        test_member_mother.mother = test_maternal_grandmother
        self.assertEqual(
            test_member.get_maternal_grandmother(), test_maternal_grandmother
        )

    def test_get_spouse_mother(self):
        test_member = Member(1, "Member", Gender.MALE)
        test_member_spouse = Member(2, "Member", Gender.FEMALE)
        test_spouse_mother = Member(3, "Spouse mother", Gender.FEMALE)

        # Error cases
        self.assertEqual(test_member.get_spouse_mother(), None)

        test_member.spouse = test_member_spouse
        self.assertEqual(test_member.get_spouse_mother(), None)

        # Success case
        test_member_spouse.mother = test_spouse_mother
        self.assertEqual(test_member.get_spouse_mother(), test_spouse_mother)

    @patch(
        "python_learning.member.Member.get_paternal_grandmother",
        side_effect=[
            None,
            create_fake_member(children=[]),
            create_fake_member(children=[Member(3, "Dad", Gender.MALE)]),
            create_fake_member(
                children=[
                    Member(3, "Dad", Gender.MALE),
                    Member(4, "Uncle", Gender.MALE),
                ]
            ),
            create_fake_member(
                children=[
                    Member(3, "Dad", Gender.MALE),
                    Member(4, "Uncle", Gender.MALE),
                    Member(5, "Aunt", Gender.FEMALE),
                ]
            ),
        ],
    )
    def test_get_paternal_aunt(self, mock_get_paternal_grandmother):
        # Simulates the function call, but should get a mock
        self.assertEqual(isinstance(self.member.get_paternal_grandmother, Mock), True)

        # Check for None values
        self.assertEqual(self.member.get_paternal_aunt(), [])
        self.assertEqual(self.member.get_paternal_aunt(), [])
        self.assertEqual(self.member.get_paternal_aunt(), [])
        self.assertEqual(self.member.get_paternal_aunt(), [])

        paternal_aunts = self.member.get_paternal_aunt()
        self.assertEqual(len(paternal_aunts), 1)
        self.assertEqual(paternal_aunts[0].id_member, 5)
        self.assertEqual(paternal_aunts[0].gender, Gender.FEMALE)

        # Check that mock_get_paternal_grandmother was called instead
        mock_get_paternal_grandmother.assert_called_with()

    # Return a fake grandmother
    @patch(
        "python_learning.member.Member.get_paternal_grandmother",
        side_effect=[
            None,
            create_fake_member(children=[]),
            create_fake_member(children=[Member(1, "Dad", Gender.MALE)]),
            create_fake_member(
                children=[
                    Member(1, "Dad", Gender.MALE),
                    Member(2, "Aunt", Gender.FEMALE),
                ],
            ),
            create_fake_member(
                children=[
                    Member(1, "Dad", Gender.MALE),
                    Member(2, "Aunt", Gender.FEMALE),
                    Member(3, "Uncle", Gender.MALE),
                ],
            ),
        ],
    )
    def test_get_paternal_uncle(self, mock_get_paternal_grandmother):
        # Simulates the function call, but should get a mock
        self.assertEqual(isinstance(self.member.get_paternal_grandmother, Mock), True)

        self.assertEqual(self.member.get_paternal_uncle(), [])
        self.assertEqual(self.member.get_paternal_uncle(), [])
        self.assertEqual(self.member.get_paternal_uncle(), [])
        self.assertEqual(self.member.get_paternal_uncle(), [])

        uncles = self.member.get_paternal_uncle()
        uncle = uncles[0]
        self.assertEqual(uncle.id_member, 3)
        self.assertEqual(uncle.gender, Gender.MALE)

        # Check that mock_get_paternal_grandmother was called instead
        mock_get_paternal_grandmother.assert_called_with()

    @patch(
        "python_learning.member.Member.get_maternal_grandmother",
        side_effect=[
            None,
            create_fake_member(children=[]),
            create_fake_member(children=[Member(1, "Mom", Gender.FEMALE)]),
            create_fake_member(
                children=[
                    Member(1, "Mom", Gender.FEMALE),
                    Member(3, "Uncle", Gender.MALE),
                ],
            ),
            create_fake_member(
                children=[
                    Member(1, "Mom", Gender.MALE),
                    Member(2, "Aunt", Gender.FEMALE),
                    Member(3, "Uncle", Gender.MALE),
                ],
            ),
        ],
    )
    def test_get_maternal_aunt(self, mock_get_maternal_grandmother):
        self.assertEqual(isinstance(self.member.get_maternal_grandmother, Mock), True)

        self.assertEqual(self.member.get_maternal_aunt(), [])
        self.assertEqual(self.member.get_maternal_aunt(), [])
        self.assertEqual(self.member.get_maternal_aunt(), [])
        self.assertEqual(self.member.get_maternal_aunt(), [])

        aunts = self.member.get_maternal_aunt()
        aunt = aunts[0]
        self.assertEqual(aunt.id_member, 2)

        # Check that mock_get_paternal_grandmother was called instead
        mock_get_maternal_grandmother.assert_called_with()

    @patch(
        "python_learning.member.Member.get_maternal_grandmother",
        side_effect=[
            None,
            create_fake_member(children=[]),
            create_fake_member(children=[Member(1, "Mom", Gender.FEMALE)]),
            create_fake_member(
                children=[
                    Member(1, "Mom", Gender.FEMALE),
                    Member(2, "Aunt", Gender.FEMALE),
                ],
            ),
            create_fake_member(
                children=[
                    Member(1, "Mom", Gender.FEMALE),
                    Member(2, "Aunt", Gender.FEMALE),
                    Member(3, "Uncle", Gender.MALE),
                ],
            ),
        ],
    )
    def test_get_maternal_uncle(self, mock_get_maternal_grandmother):
        self.assertEqual(isinstance(self.member.get_maternal_grandmother, Mock), True)

        self.assertEqual(self.member.get_maternal_uncle(), [])
        self.assertEqual(self.member.get_maternal_uncle(), [])
        self.assertEqual(self.member.get_maternal_uncle(), [])
        self.assertEqual(self.member.get_maternal_uncle(), [])

        uncles = self.member.get_maternal_uncle()
        uncle = uncles[0]
        self.assertEqual(uncle.id_member, 3)

        # Check that mock_get_paternal_grandmother was called instead
        mock_get_maternal_grandmother.assert_called_with()

    @patch(
        "python_learning.member.Member.get_spouse_mother",
        side_effect=[
            None,
            None,
            create_fake_member(children=[Member(1, "Spouse", Gender.FEMALE)]),
            create_fake_member(
                children=[
                    Member(1, "Spouse", Gender.FEMALE),
                    Member(2, "SisterInLaw", Gender.FEMALE),
                ],
            ),
            create_fake_member(
                children=[
                    Member(1, "Spouse", Gender.FEMALE),
                    Member(2, "SisterInLaw", Gender.FEMALE),
                    Member(3, "BrotherInLaw", Gender.MALE),
                ],
            ),
        ],
    )
    def test_get_brother_in_law(self, mock_get_spouse_mother):
        self.member.spouse = Member(1, "Spouse", Gender.FEMALE)
        self.assertEqual(isinstance(self.member.get_spouse_mother, Mock), True)

        self.assertEqual(self.member.get_brother_in_law(), [])
        self.assertEqual(self.member.get_brother_in_law(), [])
        self.assertEqual(self.member.get_brother_in_law(), [])
        self.assertEqual(self.member.get_brother_in_law(), [])

        brothers_in_law = self.member.get_brother_in_law()
        brother_in_law = brothers_in_law[0]
        self.assertEqual(brother_in_law.id_member, 3)

        # Check that mock_get_spouse_mother was called instead
        mock_get_spouse_mother.assert_called_with()

    @patch(
        "python_learning.member.Member.get_spouse_mother",
        side_effect=[
            None,
            create_fake_member(children=[Member(1, "Spouse", Gender.FEMALE)]),
            create_fake_member(
                children=[
                    Member(1, "Spouse", Gender.FEMALE),
                    Member(3, "BrotherInLaw", Gender.MALE),
                ],
            ),
            create_fake_member(
                children=[
                    Member(1, "Spouse", Gender.FEMALE),
                    Member(2, "SisterInLaw", Gender.FEMALE),
                    Member(3, "BrotherInLaw", Gender.MALE),
                ],
            ),
        ],
    )
    def test_get_sister_in_law(self, mock_get_spouse_mother):
        self.member.spouse = Member(1, "Spouse", Gender.FEMALE)
        self.assertEqual(isinstance(self.member.get_spouse_mother, Mock), True)

        self.assertEqual(self.member.get_sister_in_law(), [])
        self.assertEqual(self.member.get_sister_in_law(), [])
        self.assertEqual(self.member.get_sister_in_law(), [])

        sisters_in_law = self.member.get_sister_in_law()
        sister_in_law = sisters_in_law[0]
        self.assertEqual(sister_in_law.id_member, 2)

        # Check that mock_get_spouse_mother was called instead
        mock_get_spouse_mother.assert_called_with()

    def test_get_son(self):
        self.assertEqual(self.member.get_son(), [])

        demo_daugther = Member(2, "Daugther", Gender.FEMALE)
        self.member.children.append(demo_daugther)
        self.assertEqual(self.member.get_son(), [])

        demo_son = Member(3, "Son", Gender.MALE)
        self.member.children.append(demo_son)
        self.assertEqual(self.member.get_son(), [demo_son])

        self.member.children = []

    def test_get_daugther(self):
        self.assertEqual(self.member.get_daugther(), [])

        demo_son = Member(3, "Son", Gender.MALE)
        self.member.children.append(demo_son)
        self.assertEqual(self.member.get_daugther(), [])

        demo_daugther = Member(2, "Daugther", Gender.FEMALE)
        self.member.children.append(demo_daugther)
        self.assertEqual(self.member.get_daugther(), [demo_daugther])

    def test_get_siblings(self):
        self.assertEqual(self.member.get_siblings(), [])

        demo_mother = Member(1, "Mother", Gender.FEMALE)
        self.member.mother = demo_mother
        self.assertEqual(self.member.get_siblings(), [])

        self.member.mother.children = [self.member]
        self.assertEqual(self.member.get_siblings(), [])

        demo_siblings = [
            Member(3, "SiblingA", Gender.FEMALE),
            Member(4, "SiblingB", Gender.MALE),
        ]
        self.member.mother.children.extend(demo_siblings)
        self.assertEqual(self.member.get_siblings(), demo_siblings)

    @patch("python_learning.member.Member.get_siblings")
    @patch("python_learning.member.Member.get_daugther")
    @patch("python_learning.member.Member.get_son")
    @patch("python_learning.member.Member.get_sister_in_law")
    @patch("python_learning.member.Member.get_brother_in_law")
    @patch("python_learning.member.Member.get_maternal_uncle")
    @patch("python_learning.member.Member.get_maternal_aunt")
    @patch("python_learning.member.Member.get_paternal_uncle")
    @patch("python_learning.member.Member.get_paternal_aunt")
    def test_get_relationship(
        self,
        mock_get_paternal_aunt,
        mock_get_paternal_uncle,
        mock_get_maternal_aunt,
        mock_get_maternal_uncle,
        mock_get_brother_in_law,
        mock_get_sister_in_law,
        mock_get_son,
        mock_get_daugther,
        mock_get_siblings,
    ):
        self.assertRaises(
            KeyError, self.member.get_relationship, "invalid_relationship"
        )

        self.member.get_relationship("paternal_aunt")
        mock_get_paternal_aunt.assert_called_with()

        self.member.get_relationship("paternal_uncle")
        mock_get_paternal_uncle.assert_called_with()

        self.member.get_relationship("maternal_aunt")
        mock_get_maternal_aunt.assert_called_with()

        self.member.get_relationship("maternal_uncle")
        mock_get_maternal_uncle.assert_called_with()

        self.member.get_relationship("brother_in_law")
        mock_get_brother_in_law.assert_called_with()

        self.member.get_relationship("sister_in_law")
        mock_get_sister_in_law.assert_called_with()

        self.member.get_relationship("son")
        mock_get_son.assert_called_with()

        self.member.get_relationship("daugther")
        mock_get_daugther.assert_called_with()

        self.member.get_relationship("sibling")
        mock_get_siblings.assert_called_with()
