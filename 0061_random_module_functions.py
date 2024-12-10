# random module
import random

# random() function
print(random.random())

# randint() function
print(random.randint(1, 3))

# randrange() function
print(random.randrange(1, 10, 2))

# choice() function
print(random.choice([10, 23, 43, 84, 51]))

# shuffle() function
list1 = [10, 20, 30, 40, 50]
random.shuffle(list1)
print(list1)
