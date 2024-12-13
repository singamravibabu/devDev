# list sorted() function
# Syntax: sorted(list[, key=func])
# Return a new sorted list from the elements of any iterable.
cars = ['Ford', 'BMW', 'Volvo', 'Audi', 'Toyota']
new_cars = sorted(cars, key=str.upper))
print(new_cars)