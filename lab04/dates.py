from datetime import datetime
d1 = datetime.strptime(input(), "%Y-%m-%d")
d2 = datetime.strptime(input(), "%Y-%m-%d")
print(abs((d2 - d1).days))

d = datetime.strptime(input(), "%Y-%m-%d")
print(d.strftime("%A"))

import calendar
year = int(input())
print(calendar.isleap(year))

from datetime import timedelta
d = datetime.strptime(input(), "%Y-%m-%d")
n = int(input())
new_date = d + timedelta(days=n)
print(new_date.strftime("%Y-%m-%d"))

today = datetime.strptime(input(), "%Y-%m-%d")
new_year = datetime(today.year + 1, 1, 1)
print((new_year - today).days)