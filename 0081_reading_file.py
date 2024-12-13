# Read the file that doesn't exist

# throws an error as the file doesn't exist
file_obj = open("sample.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: 'sample.txt'