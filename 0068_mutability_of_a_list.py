# list is mutable

# immutable object example
def double_the_number(value):
    value = value * 2
    return value        # the new object is created

value = 25
value2 = double_the_number(value)
print(value, value2)    # 25 50


# mutable object example
def add_to_list(list, item):
    list.append(item)

list = [1, 2, 3]
add_to_list(list, 4)
print(list)