class Academics:
    def __init__(self, subject):
        self.subject = subject


class Sports:
    def __init__(self, sport):
        self.sport = sport


class Student(Academics, Sports):
    def __init__(self, subject, sport):
        Academics.__init__(self, subject)
        Sports.__init__(self, sport)

    def display(self):
        print("Subject:", self.subject)
        print("Sport:", self.sport)


s = Student("Math", "Cricket")
s.display()
