# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from tkinter.filedialog import test
from unittest import TestCase, main
from unittest.mock import patch, Mock

from python_learning.f_tree import FamilyTree
from python_learning.member import Member, Gender
from tests.unit import create_fake_member


class TestFamilyTree(TestCase):
    def setUp(self):
        self.f_tree = FamilyTree()

    def test_initialization(self):
        self.assertEqual(self.f_tree.family_tree, {})

    # Mock in the namespace you use it
    # When we import, that becomes part of our particular namespace
    @patch(
        "python_learning.f_tree.Member",
        return_value=create_fake_member(id_member=1, name="Zim", gender=Gender.MALE),
    )
    def test_add_child(self, mock_member):
        # Tree is empty
        result_initial_person = self.f_tree.add_child("Zim", Gender.MALE)
        mock_member.assert_called_with(1, "Zim", Gender.MALE)

        self.assertTrue(isinstance(self.f_tree.family_tree.get(1, "None"), Mock))
        self.assertEqual(result_initial_person, "CHILD ADDITION SUCCEDED")

        # Mother don't exist
        demo_mother = create_fake_member(
            id_member=2, name="Mother", gender=Gender.FEMALE
        )
        demo_father = create_fake_member(id_member=3, name="Father", gender=Gender.MALE)
        demo_child_name = "Zim"
        demo_child_gender = Gender.MALE

        result_person_not_found = self.f_tree.add_child(
            demo_child_name, demo_child_gender, demo_mother.__getattr__("id_member")
        )
        self.assertEqual(result_person_not_found, "PERSON NOT FOUND")

        # Father don't exist
        self.f_tree.family_tree[demo_mother.__getattr__("id_member")] = demo_mother
        result_not_mother_spouse = self.f_tree.add_child(
            demo_child_name, demo_child_gender, demo_mother.__getattr__("id_member")
        )
        self.assertEqual(result_not_mother_spouse, "CHILD ADDITION FAILED")

        # Both father and mother exist
        demo_mother_with_spouse = self.f_tree.family_tree[
            demo_mother.__getattr__("id_member")
        ]
        demo_mother_with_spouse.spouse = demo_father
        self.f_tree.family_tree[
            demo_mother.__getattr__("id_member")
        ] = demo_mother_with_spouse

        result_mother_and_father = self.f_tree.add_child(
            demo_child_name, demo_child_gender, demo_mother.__getattr__("id_member")
        )
        self.assertEqual(result_mother_and_father, "CHILD ADDITION SUCCEDED")
