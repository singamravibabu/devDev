from datetime import datetime

dt1 = "2018-01-21"
date1 = datetime.strptime(dt1, "%Y-%m-%d")
print(date1)

dt2 = "4-18, 2024 - 12:30:45"
date2 = datetime.strptime(dt2,"%m-%d, %Y - %H:%M:%S")
print(date2)

dt3 = "On the 28th day of 5th month in the year 2022 we met"
date3 = datetime.strptime(dt3, "On the %dth day of %mth month in the year %Y we met")
print(date3)