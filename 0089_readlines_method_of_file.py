# the readlines method of file object
# this method reads entire file as one list
# and each line is an element(item) of the list

# open the file in read mode, and use readlines()
with open("sample.txt", "r") as file:
    my_file = file.readlines()
    print(my_file)