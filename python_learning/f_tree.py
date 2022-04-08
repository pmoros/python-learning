from python_learning.member import Gender, Member


class FamilyTree:
    def __init__(self):
        self.family_tree = {}

    def add_child(self, name, gender, mother=0):
        _id = len(self.family_tree.keys()) + 1
        child = Member(_id, name, gender)
        mother = self.family_tree.get(mother, None)
        if not self.family_tree or not mother:
            self.family_tree[_id] = child
            return "CHILD ADDITION SUCCEDED"
        if not mother or mother.gender != Gender.FEMALE:
            return "PERSON NOT FOUND"
        if not mother.spouse:
            return "CHILD ADDITION FAILED"

        father = mother.spouse
        child.set_mother(mother)
        child.set_father(father)
        mother.add_child(child)
        father.add_child(child)
        self.family_tree[father.id_member] = father
        self.family_tree[_id] = child

        return "CHILD ADDITION SUCCEDED"
