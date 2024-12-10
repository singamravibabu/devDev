# Introduction to the list data type
# List is a collection of items in a particular order
# Lists are mutable, ordered, and can contain multiple data types
[1, 2, 3, 4, 5] # List of integers
['a', 'b', 'c', 'd', 'e'] # List of strings
[1, 'a', 2.0, 'b', 3, True] # List of mixed data types
["raju", 35, 'hr', 35000.0, 'hyd', 'executive'] # List of employee details
[] # Empty list

# Accessing elements in a list
emp = ["raju", 35, 'hr', 35000.0, 'hyd', 'executive']
print(emp[0]) # raju
print(emp[1]) # 35
print(emp[2]) # hr
print(emp[3]) # 35000.0
print(emp[4]) # hyd
print(emp[5]) # executive
# print(emp[6]) # IndexError: list index out of range

# Accessing elements from the end of the list
print(emp[-1]) # executive
print(emp[-2]) # hyd
print(emp[-3]) # 35000.0
print(emp[-4]) # hr
print(emp[-5]) # 35
print(emp[-6]) # raju
# print(emp[-7]) # IndexError: list index out of range

# Creating a list with default values using repetition operator
# Syntax: [value] * n
scores = [0] * 5
print(scores) # [0, 0, 0, 0, 0]