countries = {"IN":'India',
                 "US":'United States', 
                 "UK":'United Kingdom', 
                 "AU":'Australia'}

# print(countries['NZ']) # KeyError: 'NZ'

# get() method prevents KeyError
# Syntax: dictionary.get(key)
print(countries.get('NZ')) # None
print(countries.get('JP', "Not Known Country")) # India