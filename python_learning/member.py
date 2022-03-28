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
        else:
            self.children.append(child)
