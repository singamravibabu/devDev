# Example 1: Simple global variable
x = 10  # Global variable

def print_global():
    print(x)  # Accessing global variable

print_global()  # Output: 10

# Example 2: Local variable inside a function
def print_local():
    y = 20  # Local variable
    print(y)

print_local()  # Output: 20
# print(y)  # This would raise a NameError because y is not defined outside the function

# Example 3: Modifying global variable inside a function using global keyword
z = 30  # Global variable

def modify_global():
    global z
    z = 40  # Modifying global variable

modify_global()
print(z)  # Output: 40

# Example 4: Local variable with the same name as global variable
a = 50  # Global variable

def local_same_name():
    a = 60  # Local variable with the same name as global variable
    print(a)  # Output: 60

local_same_name()
print(a)  # Output: 50

# Example 5: Accessing global variable inside a function without modifying it
b = 70  # Global variable

def access_global():
    print(b)  # Accessing global variable

access_global()  # Output: 70