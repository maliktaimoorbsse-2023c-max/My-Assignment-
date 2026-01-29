class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("Sara", 20)
s.display()

