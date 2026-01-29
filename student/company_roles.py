class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    pass


class Manager(Employee):
    def display(self):
        print("Manager Name:", self.name)


m = Manager("Usman")
m.display()

