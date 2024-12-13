# the 'read' method of the file

# open the file
with open('sample.txt', 'r') as file:
    # read() method reads the entire file as one string
    content = file.read()
    print(content)
