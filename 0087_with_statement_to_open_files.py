# the 'with' statement is used to open files
# it is a good practice to use 'with' statement to open files
# because it automatically closes the file when the block is exited
# so there is no need to explicitly close the file
# the 'with' statement is used to open files

with open("sample.txt", "r") as file:
    print(file.read())