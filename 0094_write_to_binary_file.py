# a binary file: is non-text file
# binary files are used for saving images, videos, executables, etc.
# binary files are not human readable
# To work with binary files we use 'pickle' module
# 'pickle' provides methods for serializing and deserializing objects
# dump(write) to write an object to a file
# load(read) to read an object from a file
# object can be list, tuple, image, dictionary, etc.
import pickle

books = [
    ['One Minute Manager', 'Kenneth Blanchard', 111],
    ['Leaders', 'Warren Bennis', 222],
    ['The Alchemist', 'Paulo Coelho', 333],
    ['The Monk Who Sold His Ferrari', 'Robin Sharma', 444],
    ['The Power of Now', 'Eckhart Tolle', 555],    
]

# dump(object, file) writes the object to the file
with open('books.bin', 'wb') as file:
    pickle.dump(books, file)