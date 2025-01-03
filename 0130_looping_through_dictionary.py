countries = {"IN":'India',
                 "US":'United States', 
                 "UK":'United Kingdom', 
                 "AU":'Australia',
                 "CA":'Canada',
                 "NZ":'New Zealand',
                 "DE":'Germany',}

# print all keys using the loop
for k in countries:
    print(k)
    
# print all keys using the loop keys()
for k in countries.keys():
    print(k)
    
# print all values using the loop using values()
for v in countries.values():
    print(v)
    
# print all items using the loop using items()
for kv in countries.items():
    print(kv)