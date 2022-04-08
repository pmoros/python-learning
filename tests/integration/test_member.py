from unittest import TestCase
from python_learning.member import Gender, Member


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", Gender.MALE)
        self.mother = Member(2, "Mother", Gender.FEMALE)
        self.father = Member(3, "Father", Gender.MALE)
        self.mother_sister_a = Member(4, "MaternalAuntA", Gender.FEMALE)
        self.mother_sister_b = Member(5, "MaternalAuntB", Gender.FEMALE)
        self.mother_brother_a = Member(4, "MaternalUncleA", Gender.MALE)
        self.mother_brother_b = Member(5, "MaternalUncleB", Gender.MALE)
        self.father_sister_a = Member(6, "PaternalAuntA", Gender.FEMALE)
        self.father_sister_b = Member(7, "PaternalAuntB", Gender.FEMALE)
        self.father_brother_a = Member(8, "PaternalUncleA", Gender.MALE)
        self.father_brother_b = Member(9, "PaternalUncleB", Gender.MALE)
        self.spouse = Member(10, "Spouse", Gender.FEMALE)
        self.spouse_sister_a = Member(11, "SpouseSisterA", Gender.FEMALE)
        self.spouse_sister_b = Member(12, "SpouseSisterB", Gender.FEMALE)
        self.spouse_brother_a = Member(13, "SpouseBrotherA", Gender.MALE)
        self.spouse_brother_b = Member(14, "SpouseBrotherB", Gender.MALE)
        self.brother_a = Member(15, "BrotherA", Gender.MALE)
        self.brother_b = Member(16, "BrotherB", Gender.MALE)
        self.sister_a = Member(17, "SisterA", Gender.FEMALE)
        self.sister_b = Member(18, "SisterB", Gender.FEMALE)
        self.son_a = Member(19, "SonA", Gender.MALE)
        self.son_b = Member(20, "SonB", Gender.MALE)
        self.daugther_a = Member(21, "DaugtherA", Gender.FEMALE)
        self.daugther_b = Member(22, "DaugtherB", Gender.FEMALE)
        self.maternal_grandmother = Member(23, "MaternalGrandmother", Gender.FEMALE)
        self.paternal_grandmother = Member(24, "PaternalGrandmother", Gender.FEMALE)
        self.spouse_grandmother = Member(25, "SpouseGrandmother", Gender.FEMALE)

        # Add parents
        self.member.set_mother(self.mother)
        self.member.set_father(self.father)
        # Add spouse
        self.member.father.set_spouse(self.mother)

        self.member.father.add_child(self.member)
        self.member.mother.add_child(self.member)

        # Add siblings
        self.member.father.add_child(self.brother_a)
        self.member.father.add_child(self.brother_b)
        self.member.father.add_child(self.sister_a)
        self.member.father.add_child(self.sister_b)
        self.member.mother.add_child(self.brother_a)
        self.member.mother.add_child(self.brother_b)
        self.member.mother.add_child(self.sister_a)
        self.member.mother.add_child(self.sister_b)

        # Add paternal aunt/uncles
        self.member.father.set_mother(self.paternal_grandmother)
        self.paternal_grandmother.add_child(self.father)
        self.paternal_grandmother.add_child(self.father_brother_a)
        self.paternal_grandmother.add_child(self.father_brother_b)
        self.paternal_grandmother.add_child(self.father_sister_a)
        self.paternal_grandmother.add_child(self.father_sister_b)

        # Add maternal aunt/uncles
        self.member.mother.set_mother(self.maternal_grandmother)
        self.maternal_grandmother.add_child(self.mother)
        self.maternal_grandmother.add_child(self.mother_brother_a)
        self.maternal_grandmother.add_child(self.mother_brother_b)
        self.maternal_grandmother.add_child(self.mother_sister_a)
        self.maternal_grandmother.add_child(self.mother_sister_b)

        # Add spouse
        self.member.set_spouse(self.spouse)

        # Add spouse brothers/sisters
        self.spouse.set_mother(self.spouse_grandmother)
        self.spouse_grandmother.add_child(self.spouse)
        self.spouse_grandmother.add_child(self.spouse_brother_a)
        self.spouse_grandmother.add_child(self.spouse_brother_b)
        self.spouse_grandmother.add_child(self.spouse_sister_a)
        self.spouse_grandmother.add_child(self.spouse_sister_b)

        # Add our sons and daughters
        self.member.add_child(self.son_a)
        self.member.add_child(self.son_b)
        self.member.add_child(self.daugther_a)
        self.member.add_child(self.daugther_b)

    def test_set_methods(self):

        # Test parents
        self.assertEqual(self.member.mother.name, "Mother")
        self.assertEqual(self.member.father.name, "Father")
        self.assertTrue(self.member in self.member.father.children)
        self.assertTrue(self.member in self.member.mother.children)

        # Test siblings
        self.assertEqual(
            len(self.member.mother.children), 5
        )  # Includes the member itself

        # Test spouse
        self.assertEqual(self.member.spouse, self.spouse)

        # Test paternal/maternal aunts and uncles
        self.assertEqual(len(self.member.get_maternal_grandmother().children), 5)
        self.assertEqual(len(self.member.get_paternal_grandmother().children), 5)

        # Test children
        self.assertEqual(len(self.member.get_son()), 2)
        self.assertEqual(len(self.member.get_daugther()), 2)

    def test_get_relationship_methods(self):
        self.assertEqual(len(self.member.get_relationship("paternal_aunt")), 2)
        self.assertEqual(len(self.member.get_relationship("paternal_uncle")), 2)
        self.assertEqual(len(self.member.get_relationship("maternal_aunt")), 2)
        self.assertEqual(len(self.member.get_relationship("maternal_uncle")), 2)
        self.assertEqual(len(self.member.get_relationship("brother_in_law")), 2)
        self.assertEqual(len(self.member.get_relationship("sister_in_law")), 2)
        self.assertEqual(len(self.member.get_relationship("son")), 2)
        self.assertEqual(len(self.member.get_relationship("daugther")), 2)
        self.assertEqual(len(self.member.get_relationship("sibling")), 4)
