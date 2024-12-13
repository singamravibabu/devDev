# from random module choice and shuffle functions
import random

my_list = [10, 85, 99, 43, 29, 'a', 'b', 'c', 'd', 'e']
pick1 = random.choice(my_list)
pick2 = random.choice(my_list)
pick3 = random.choice(my_list)
pick4 = random.choice(my_list)

print(pick1)
print(pick2)
print(pick3)
print(pick4)

# shuffle the list
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)