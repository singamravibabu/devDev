# use deepcopy from copy module to copy a list
# deepcopy will copy all the elements of the list
# and create a new list with new memory location
# so that changes in the new list will not affect the original list
import copy

# create a list
list1 = [1, 2, 3]

# deepcopy of list1
list2 = copy.deepcopy(list1)

# change lists
list1[0] = 4
list2[0] = 5

# print lists
print("list1:", list1)
print("list2:", list2)
