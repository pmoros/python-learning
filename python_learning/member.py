"""
Defines Member class and it's dependencies.
Typical usage example:

member_gender = Gender.MALE
some_member = Member(1, "member_name", member_gender)
# Manipulate the member
"""
from enum import Enum


class Gender(Enum):
    """Defines allowed gender."""

    MALE = "MALE"
    FEMALE = "FEMALE"


class Member:
    """
    Defines a Member.

    Args:
    id: unique identifier to a member (int)
    name: str
    gender: Gender
    """

    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.__set_gender(gender)
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    def __set_gender(self, gender):
        if not isinstance(gender, Gender):
            raise TypeError("Non valid value for gender")

        self.gender = gender

    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise TypeError("Invalid value for mother")

        if mother.gender != Gender.FEMALE:
            raise ValueError(
                "Invalid gender value for mother" "Mother should be .FEMALE"
            )

        self.mother = mother

    def set_father(self, father):
        if not isinstance(father, Member):
            raise TypeError("Invalid value for father")

        if father.gender != Gender.MALE:
            raise ValueError(
                "Invalid gender value for father. " "Father should be male"
            )

        self.father = father

    def set_spouse(self, spouse):
        """Handles the necessary rules so a spouse can be assigned."""
        if not isinstance(spouse, Member):
            raise TypeError("Invalid value for spouse")

        if spouse.gender == self.gender:
            raise ValueError(
                "Invalid spouse value. " "Spouse should be of the opposite genre"
            )

        self.spouse = spouse

    def add_child(self, child):
        """Handles the necessary rules to assign a child to a member."""
        if not isinstance(child, Member):
            raise TypeError("Invalid value for child")

        if (self.gender != Gender.FEMALE) and self.spouse is None:
            raise AttributeError("It's not possible to add a child")

        self.children.append(child)

    def get_paternal_grandmother(self):
        if not self.father:
            return None
        if not self.father.mother:
            return None

        return self.father.mother

    def get_maternal_grandmother(self):
        if not self.mother:
            return None
        if not self.mother.mother:
            return None

        return self.mother.mother

    def get_spouse_mother(self):
        if not self.spouse:
            return None
        if not self.spouse.mother:
            return None

        return self.spouse.mother

    def get_paternal_aunt(self):
        aunts = []
        paternal_grandmother = self.get_paternal_grandmother()
        if not paternal_grandmother:
            return []

        grandmother_children = paternal_grandmother.children
        aunts = list(filter(lambda x: x.gender == Gender.FEMALE, grandmother_children))

        return aunts

    def get_paternal_uncle(self):
        uncles = []
        paternal_grandmother = self.get_paternal_grandmother()
        if not paternal_grandmother:
            return []

        grandmother_children = paternal_grandmother.children

        male_children = list(
            filter(lambda x: x.gender == Gender.MALE, grandmother_children)
        )

        uncles = list(filter(lambda x: x.id != self.father.id, male_children))

        return uncles

    def get_maternal_aunt(self):
        aunts = []
        maternal_grandmother = self.get_maternal_grandmother()
        if not maternal_grandmother:
            return []
        grandmother_children = maternal_grandmother.children

        female_children = list(
            filter(lambda x: x.gender == Gender.FEMALE, grandmother_children)
        )

        aunts = list(filter(lambda x: x.id != self.mother.id, female_children))

        return aunts

    def get_maternal_uncle(self):
        uncles = []
        maternal_grandmother = self.get_maternal_grandmother()
        if not maternal_grandmother:
            return []

        grandmother_children = maternal_grandmother.children
        uncles = list(filter(lambda x: x.gender == Gender.MALE, grandmother_children))

        return uncles

    def get_brother_in_law(self):
        spouse_mother = self.get_spouse_mother()
        if not spouse_mother:
            return []

        spouse_mother_children = spouse_mother.children
        brothers_in_law = list(
            filter(lambda x: x.gender == Gender.MALE, spouse_mother_children)
        )
        if self.spouse.gender == Gender.MALE:
            brothers_in_law = filter(lambda x: x != self.spouse, brothers_in_law)

        return brothers_in_law

    def get_sister_in_law(self):
        sisters_in_law = []
        spouse_mother = self.get_spouse_mother()
        if not spouse_mother:
            return []

        spouse_mother_children = spouse_mother.children
        sisters_in_law = list(
            filter(lambda x: x.gender == Gender.FEMALE, spouse_mother_children)
        )
        if self.spouse.gender == Gender.FEMALE:
            sisters_in_law = list(
                filter(lambda x: x.id != self.spouse.id, sisters_in_law)
            )

        return sisters_in_law

    def get_son(self):
        if not self.children:
            return []

        sons = list(filter(lambda x: x.gender == Gender.MALE, self.children))
        return sons

    def get_daugther(self):
        if not self.children:
            return []

        daugther = list(filter(lambda x: x.gender == Gender.FEMALE, self.children))
        return daugther

    def get_siblings(self):
        if not self.mother or not self.mother.children:
            return []

        siblings = list(filter(lambda x: x != self, self.mother.children))
        return siblings
