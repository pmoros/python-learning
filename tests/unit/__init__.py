"""
    Shared functionality for the unit tests.
"""
from unittest.mock import Mock


def create_fake_member(
    id_member=None,
    name=None,
    gender=None,
    mother=None,
    father=None,
    spouse=None,
    children=None,
):
    member = Mock()
    member.id_member = id_member
    member.name = name
    member.gender = gender
    member.mother = mother
    member.father = father
    member.spouse = spouse
    member.children = children

    return member
