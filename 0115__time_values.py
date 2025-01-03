import datetime

# Create a time object
# datetime.time(hh, mm, ss, ms) - all parameters are optional
login_time = datetime.time(10, 45)
print(f"Login time: {login_time}")

# alternatively
from datetime import time
logout_time = time(17, 30, 45)
print(f"Logout time: {logout_time}")
