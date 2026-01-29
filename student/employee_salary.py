class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, new_salary):
        self.__salary = new_salary

    def display_salary(self):
        print("Salary:", self.__salary)


e = Employee(50000)
e.update_salary(60000)
e.display_salary()
