from unittest import TestCase
from python_learning.member import Member


class TestMember(TestCase):
    def setUp(self):
        self.member = Member()

    def test_initialization(self):
        self.assertEqual(isinstance(self.member, Member), True)
