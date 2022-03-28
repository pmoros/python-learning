from multiprocessing.sharedctypes import Value
from unittest import TestCase
from python_learning.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", Gender.male)

    def test_initialization(self):
        # Check instance
        self.assertEqual(isinstance(self.member, Member), True)

        # Check properties
        self.assertEqual(self.member.id, 1)
        self.assertEqual(self.member.name, "Zim")
        self.assertEqual(self.member.gender, Gender.male)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.father, None)
        self.assertEqual(self.member.spouse, None)
        self.assertEqual(self.member.children, [])

    def test_set_mother(self):
        mother_demo_a = "mother_demo_a"  # Wrong type
        mother_demo_b = Member(2, "MotherDemoB", Gender.male)  # Invalid sex
        mother_demo_c = Member(3, "Mom", Gender.female)

        # Error case
        self.assertRaises(TypeError, self.member.set_mother, mother_demo_a)
        self.assertRaises(ValueError, self.member.set_mother, mother_demo_b)

        # Success case
        self.member.set_mother(mother_demo_c)
        self.assertEqual(self.member.mother.name, "Mom")
        self.assertEqual(self.member.mother.gender, Gender.female)

    def test_set_father(self):
        father_demo_a = "father_demo_a"  # Wrong type
        father_demo_b = Member(2, "FatherDemoB", Gender.female)  # Invalid sex
        father_demo_c = Member(3, "Dad", Gender.male)

        # Error case
        self.assertRaises(TypeError, self.member.set_father, father_demo_a)
        self.assertRaises(ValueError, self.member.set_father, father_demo_b)

        # Success case
        self.member.set_father(father_demo_c)
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member.father.gender, Gender.male)

    def test_set_spouse(self):
        spouse_demo_a = "SpouseA"
        spouse_demo_b = Member(4, "MaleB", Gender.male)
        spouse_demo_c = Member(5, "WomanC", Gender.female)

        # Error case
        self.assertRaises(TypeError, self.member.set_spouse, spouse_demo_a)
        self.assertRaises(ValueError, self.member.set_spouse, spouse_demo_b)

        # Success case
        self.member.set_spouse(spouse_demo_c)
        self.assertNotEqual(self.member.spouse.gender, self.member.gender)

    def test_add_child(self):
        child_demo_a = "ChildA"
        child_demo_b = Member(6, "ChildB", Gender.male)

        # Error case
        self.assertRaises(TypeError, self.member.add_child, child_demo_a)
        self.assertRaises(AttributeError, self.member.add_child, child_demo_b)

        # Success case
        member_female = Member(7, "FemaleAux", Gender.female)
        member_female.set_spouse(self.member)
        member_female.add_child(child_demo_b)
        self.assertEqual(member_female.children.pop(), child_demo_b)
