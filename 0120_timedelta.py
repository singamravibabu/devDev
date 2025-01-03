from datetime import date, time, datetime, timedelta

# Create a timedelta object
# timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds)
six_weeks = timedelta(weeks=6)
print(six_weeks.days)

five_days = timedelta(days=5)
print(five_days.days)

five_days_4_hours = timedelta(days=5, hours=4)
print(five_days_4_hours)

time_span = timedelta(days=5, hours=4, minutes=3, seconds=2)
print(time_span)
