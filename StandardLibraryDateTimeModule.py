import datetime
import calendar
import os

today = datetime.date.today()
print(today)

print(calendar.isleap(2016))

# getting current directory we r in
print(os.getcwd())
print(os.__file__)