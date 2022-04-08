from readline import get_begidx
from unittest import TestCase

from python_learning.member import Member, Gender
from python_learning.f_tree import FamilyTree


class TestFamilyTree(TestCase):
    def setUp(self):
        self.f_tree = FamilyTree()
        self.mother = Member(0, "Mother", Gender.FEMALE)
        self.father = Member(0, "Father", Gender.MALE)
        self.child = Member(0, "Child", Gender.MALE)

    def test_add_child(self):

        # Include the fathers into the family tree
        self.f_tree.add_child(self.mother.name, self.mother.gender)
        self.f_tree.add_child(self.father.name, self.father.gender)
        self.f_tree.family_tree[1].set_spouse(self.f_tree.family_tree[2])
        self.f_tree.family_tree[2].set_spouse(self.f_tree.family_tree[1])

        # Try to add the child
        self.f_tree.add_child(self.child.name, self.child.gender, 1)

        result_member = self.f_tree.family_tree[3]
        self.assertEqual(result_member.id_member, 3)
        self.assertEqual(self.f_tree.family_tree[1].children[0].id_member, 3)
        self.assertEqual(self.f_tree.family_tree[2].children[0].id_member, 3)
