# list methods help to manipulate the list
# Syntax: list.method()

# Creating a list
stationary_items = ['pen', 'pencil', 'eraser', 'sharpner', 'scale']

# append(element) method: adds an element at the end of the list
stationary_items.append('notebook')
print(stationary_items)
stationary_items.append('colors')
print(stationary_items)
stationary_items.append('glue')
print(stationary_items)

# insert(index, element) method: adds an element at the specified index
stationary_items.insert(2, 'compass')
print(stationary_items)
stationary_items.insert(5, 'stapler')
print(stationary_items)

# index(element) method: returns the index of the first occurance of the specified element
stationary_items.append('compass')
print(stationary_items)
index = stationary_items.index('compass')
print(index)

# remove(element) method: removes the first occurance of the specified element
stationary_items.remove('compass')
print(stationary_items)
stationary_items.remove('stapler')
print(stationary_items)

# pop([index]) method: removes the element at the specified index, and if the index specified, removes the last element
# before removing the element, it returns the element
element = stationary_items.pop()
print(element)
print(stationary_items)
element = stationary_items.pop(2)
print(element)
print(stationary_items)

# count(element) method: returns the number of occurances of the specified element
count = stationary_items.count('pen')
print(count)
count = stationary_items.count('compass')
print(count)