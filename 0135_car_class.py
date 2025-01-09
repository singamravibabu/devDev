class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start_engine(self):
        print(f'{self.brand} {self.model} engine started')
        
    def stop_engine(self):
        print(f'{self.brand} {self.model} engine stopping...')
        
my_car = Car('Ford', 'Mustang', 2021)
your_car = Car('Toyota', 'Corolla', 2020)
print(my_car.brand)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()