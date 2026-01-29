class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)


s = Student("Ali", 85)
s.display()
