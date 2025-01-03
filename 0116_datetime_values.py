import datetime

# Create a datetime object
# datetime.datetime(year, month, day, hour, minute, second, microsecond)
# all time arguments are optional
yearly_meet = datetime.datetime(2024, 4, 14, 11, 30, 0, 0)

# alternatively
from datetime import datetime
next_year_meet = datetime(2025, 4, 14, 11, 30, 0, 0)

# now() method returns the current date and time
now = datetime.now()

# print all the values
print(f"Yearly meet: {yearly_meet}")
print(f"Next year meet: {next_year_meet}")
print(f"Current date and time: {now}")