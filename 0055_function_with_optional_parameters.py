# function definition: three parameters
def product(name, price, discountPercent):
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Discount percent: {discountPercent}")
    print(f"Discount amount: {price * discountPercent / 100}")
    print(f"Discount price: {price - (price * discountPercent / 100)}")