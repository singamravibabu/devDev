# Create Decimal objects
# from decimal module import the 'Decimal' class to create Decimal objects
# Unlike float, Decimal objects are not floating point numbers

x = 100.1
y = x + x + x
print(y)

# The Decimal numbers are more accurate than float numbers
from decimal import Decimal
a = Decimal('100.1')
b = a + a + a
print(f"Value of b: {b}")
