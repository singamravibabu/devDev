# the readline method of file
# the readline() method reads the next line

with open("sample.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    print(line1, end="")
    print(line2, end="")
    print(line3, end="")