# split([delimiter][, num]) method splits strings based on a delimiter
# By default, the delimiter is a space

# Example 1
quote = "I am a Python programmer"
words = quote.split()
print(words)  # ['I', 'am', 'a', 'Python', 'programmer']

# Example 2
date = "23/12/2019"
date_components = date.split("/")
print(date_components)  # ['23/12/2019']
