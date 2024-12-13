# opening a file in read mode, and the file exists
file = open("test.txt", "r")

# reading using read() method
print(file.read())
file.close()
print()

# using for loop to read line by line
file = open("test.txt", "r")
for line in file:
    print(line, end="")
    
# closing the file
file.close()