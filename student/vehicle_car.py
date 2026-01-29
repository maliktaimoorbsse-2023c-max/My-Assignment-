class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


c = Car("Toyota", "Corolla")
c.display()
