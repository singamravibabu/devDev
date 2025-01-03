from datetime import date, time, datetime, timedelta

# A timedelta object stores a span of time
number_of_days = date(2025, 3, 8) - date(2024, 12, 30)
print(number_of_days.days)  # 68
waiting_time = datetime(2024,12, 30, 18, 30) - datetime(2024, 12, 30, 16, 25)
print(waiting_time)  # 2:05:00 