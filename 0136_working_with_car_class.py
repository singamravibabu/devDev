from car import Car

my_car = Car('Ford', 'Mustang', 2021)
your_car = Car('Toyota', 'Corolla', 2020)

print("My car details....")
print(my_car.brand)
print(my_car.model)
print(my_car.year)
print()

print("Your car details....")
print(your_car.brand)
print(your_car.model)
print(your_car.year)
print()

my_car.start_engine()
my_car.stop_engine()
print()

your_car.start_engine()
your_car.stop_engine()
