# the strftime() format codes:
# %a - abbreviated weekday name
# %A - full weekday name
# %b - abbreviated month name
# %B - full month name
# %c - preferred date and time representation
# %C - century number (the year divided by 100, range 00 to 99)
# %d - day of the month (01 to 31)
## %D - same as %m/%d/%y
# %H - hour in 24-hour format (00 to 23)
# %I - hour in 12-hour format (01 to 12)
# %j - day of the year (001 to 366)
# %m - month (01 to 12)
# %M - minute
# %p - AM/PM indicator
# %S - second
from datetime import datetime

dt1 = datetime(2018, 1, 21, 15, 45, 30)
date1 = dt1.strftime("%Y-%b-%d (%a)")
print(f"Date 1: {date1}")
date2 = dt1.strftime("%A - %B %d, %Y")
print(f"Date 2: {date2}")
date3 = dt1.strftime("%d %B %Y - %I:%M:%S %p")
print(f"Date 3: {date3}")

dt2 = datetime.now()
date4 = dt2.strftime("%B-%d, %Y (%A) - %I:%M:%S %p")
print(f"Date 4: {date4}")