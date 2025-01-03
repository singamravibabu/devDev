import datetime

# Create a date object
# datetime.date(yyyy, mm, dd)
meeting_date = datetime.date(2025, 1, 4)

# alternatively
from datetime import date
holidays_start_date = date(2025, 3, 25)

# today() method for current date
eeroju = date.today()

# printing all the dates
print(f"Meeting date: {meeting_date}")
print(f"Holidays start date: {holidays_start_date}")
print(f"Today's date: {eeroju}")
