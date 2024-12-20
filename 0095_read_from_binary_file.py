# read a binary file
# use 'load' function from pickle module
# load(file) to read an object from a file
import pickle

# open the file in read-binary mode
with open('books.bin', 'rb') as file:
    data = pickle.load(file)
    print(data)