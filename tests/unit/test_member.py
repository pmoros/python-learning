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

        # Edge case for gender

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
