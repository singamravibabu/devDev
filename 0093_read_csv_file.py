# reading a csv file
# to read data from a csv file use reader() function from csv module
# use for loop to read data from csv file
import csv

with open('emp_data.csv', 'r', newline='') as file:
    # reader() function returns a reader object
    r_obj = csv.reader(file)
    for line in r_obj:
        # print(line)
        print(f"{line[0]} -\t {line[2]}")