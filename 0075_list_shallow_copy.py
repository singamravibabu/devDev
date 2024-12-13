# list shallow copying
# a shallow copy doesn't creates a new object

my_list = ["anand", "kumar", "singh"]

# shallow copy
new_list = my_list

# changing the new_list
new_list.append("java")

# changing the my_list
my_list.append("r language")

# printing the lists
print(my_list)
print(new_list)