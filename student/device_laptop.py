class Device:
    def __init__(self, brand):
        self.brand = brand


class Computer(Device):
    pass


class Laptop(Computer):
    def display(self):
        print("Brand:", self.brand)


l = Laptop("Dell")
l.display()
