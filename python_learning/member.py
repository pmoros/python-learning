from enum import Enum


class Gender(Enum):
    male = "Male"
    female = "Female"


class Member:
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
        else:
            self.gender = gender

    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise TypeError("Invalid value for mother")
        elif mother.gender != Gender.female:
            raise ValueError(
                "Invalid gender value for mother" "Mother should be female"
            )
        else:
            self.mother = mother

    def set_father(self, father):
        if not isinstance(father, Member):
            raise TypeError("Invalid value for father")
        elif father.gender != Gender.male:
            raise ValueError(
                "Invalid gender value for father. " "Father should be male"
            )
        else:
            self.father = father

    def set_spouse(self, spouse):
        if not isinstance(spouse, Member):
            raise TypeError("Invalid value for spouse")
        elif spouse.gender == self.gender:
            raise ValueError(
                "Invalid spouse value. " "Spouse should be of the opposite genre"
            )
        else:
            self.spouse = spouse

    def add_child(self, child):
        if not isinstance(child, Member):
            raise TypeError("Invalid value for child")
        if (self.gender == Gender.female) and self.spouse is not None:
            self.children.append(child)
        else:
            raise AttributeError("It's not possible to add a child")
