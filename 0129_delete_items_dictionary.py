# Delete Items from dictionary
# 'del' keyword, pop() method, clear() method

countries = {"IN":'India',
                 "US":'United States', 
                 "UK":'United Kingdom', 
                 "AU":'Australia',
                 "CA":'Canada',
                 "NZ":'New Zealand',
                 "DE":'Germany',}

# del keyword - delete item with key 'AU'
del countries["AU"]
print(countries)

# pop() method - delete item with key 'CA'
countries.pop("CA")
print(countries)

# clear() method - delete all items
countries.clear()
print(countries)