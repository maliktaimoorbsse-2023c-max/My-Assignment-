class Grandparent:
    def __init__(self, family_name):
        self.family_name = family_name


class Parent(Grandparent):
    def __init__(self, family_name, parent_name):
        super().__init__(family_name)
        self.parent_name = parent_name


class Child(Parent):
    def __init__(self, family_name, parent_name, child_name):
        super().__init__(family_name, parent_name)
        self.child_name = child_name

    def display(self):
        print("Family Name:", self.family_name)
        print("Parent Name:", self.parent_name)
        print("Child Name:", self.child_name)


c = Child("Khan", "Ahmed", "Ali")
c.display()
