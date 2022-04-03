# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from tkinter.filedialog import test
from unittest import TestCase, main

from python_learning.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", Gender.MALE)

    def test_initialization(self):
        # Check instance
        self.assertEqual(isinstance(self.member, Member), True)

        # Check properties
        self.assertEqual(self.member.id, 1)
        self.assertEqual(self.member.name, "Zim")
        self.assertEqual(self.member.gender, Gender.MALE)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.father, None)
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


if __name__ == "__main__":
    main()
