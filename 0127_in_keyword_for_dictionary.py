# Checking whether a key is in a dictionary
# The 'in' keyword used to check whether a key is in a dictionary.
# Syntax: key in dictionary
# It returns True if the key is in the dictionary, False otherwise.

countries = {"IN":'India',
                 "US":'United States', 
                 "UK":'United Kingdom', 
                 "AU":'Australia'}

# Check if 'IN' is in the dictionary
if 'IN' in countries:
    print("IN is in the dictionary")
    
if 'JP' in countries:
    print("JP is in the dictionary")
else:
    print("JP is not in the dictionary")