# attributes that return parts of date/time object
from datetime import datetime

dt = datetime(2025, 1, 10, 17, 30, 45, 112233)

# year
print(dt.year)  # 2025

# month
print(dt.month) # 1

# day
print(dt.day)   # 10

# hour
print(dt.hour)  # 17

# minute
print(dt.minute) # 30

# second
print(dt.second) # 45

# microsecond
print(dt.microsecond) # 0
