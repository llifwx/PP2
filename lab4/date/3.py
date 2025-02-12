import datetime

current_time = datetime.datetime.now().replace(microsecond=0)
print("Current datetime without microseconds:", current_time)