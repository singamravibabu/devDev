# function definition: three parameters; one is optional
def product(name, price, discountPercent=10):
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Discount percent: {discountPercent}")
    print(f"Discount amount: {price * discountPercent / 100}")
    print(f"Discount price: {price - (price * discountPercent / 100)}")

product("Laptop", 50000, 20)