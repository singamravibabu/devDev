# Writing data to a csv file.
# to work with csv files import 'csv' module
import csv

books = [
    ['Title', 'Author', 'Genre'],
    ['Python Basics', 'Bill Smith', 'Programming'],
    ['Python Cookbook', 'Ian Smith', 'Programming'],
    ['Python for Dummies', 'John Smith', 'Programming'],
    ['Python for Kids', 'David Smith', 'Programming'],
    ['Python for Data Science', 'James Smith', 'Programming'],
    ['Python for Machine Learning', 'Robert Smith', 'Programming'],
    ['Python for Artificial Intelligence', 'Michael Smith', 'Programming'],
]

# create writer object using writer() function from csv module
# use writerows() method to write data to csv file
with open('books.csv', 'w', newline='') as file:
    w_obj = csv.writer(file)
    w_obj.writerows(books)