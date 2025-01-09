# convert between dictionaries and lists
countries = {"IN":'India',
                 "US":'United States', 
                 "UK":'United Kingdom', 
                 "AU":'Australia',
                 "CA":'Canada',
                 "NZ":'New Zealand',
                 "DE":'Germany',}

dkeys = list(countries.keys())  # convert keys to list
print(dkeys)                # ['IN', 'US', 'UK', 'AU', 'CA', 'NZ', 'DE']

dvalues = list(countries.values())  # convert values to list
print(dvalues)              # ['India', 'United States', 'United Kingdom', 'Australia', 'Canada', 'New Zealand', 'Germany']

ditems = list(countries.items())
print(ditems)

numbers = [[1, 'one'],
           [2, 'two'],
           [3, 'three'],
           [4, 'four'],
           [5, 'five'],
           [6, 'six'],
           [7, 'seven'],
           [8, 'eight'],
           [9, 'nine'],
           [10, 'ten']]

number_dict = dict(numbers)
print(number_dict)
