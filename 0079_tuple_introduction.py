# tuple
# A tuple is a collection which is ordered items and unchangeable (immutable).
# In Python tuples are written with round brackets.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Syntax: tuple_name = (item1, item2, item3, item4, item5)

# Example 1
depts = ("IT", "HR", "Finance", "Admin", "Sales")
print(depts)

# Accessing items in a tuple using index number
print(depts[0])  # Output: IT
print(depts[1])  # Output: HR
print(depts[-1])  # Output: Sales
print(depts[-2])  # Output: Admin

# once a tuple is created, we can't add, remove, or set items
depts[0] = "IT Support"  # TypeError: 'tuple' object does not support item assignment