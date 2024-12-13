# list sort() method
# The sort() method sorts the list ascending by default.
# Syntax: list.sort(reverse=True|False, key=func)
books = ['Python', 'java', 'C++', 'C#', 'Ruby', 'PHP']
books.sort() # None
print(books)
books.sort(key=str.lower)   # books.sort(key=str.upper)
print(books)