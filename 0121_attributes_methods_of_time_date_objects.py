from datetime import date, time, datetime, timedelta

# attributos of timedelta
print('Attributes of timedelta')
td = timedelta(weeks=2, days=3, hours=15, minutes=7)
print('days:', td.days)
print('seconds:', td.seconds)
print('microseconds:', td.microseconds)

# totalseconds() method
print(td.total_seconds())