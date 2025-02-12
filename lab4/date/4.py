import datetime

date1 = datetime.datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime.datetime(2024, 2, 11, 12, 0, 0)

a = date2 - date1
print("Difference in seconds:", a.total_seconds())
