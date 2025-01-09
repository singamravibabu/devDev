# Define a class named 'Car'
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

c1 = Car('Toyota', 'Corolla', 2019)
c1.model = 'Camry'
c1.year = 2020
print(c1.brand)
print(c1.model)
print(c1.year)