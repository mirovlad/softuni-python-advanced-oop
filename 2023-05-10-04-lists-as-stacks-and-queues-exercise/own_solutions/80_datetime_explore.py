import datetime

datetime1 = datetime.datetime.strptime("8:00:00", "%H:%M:%S")
print("datetime", datetime1)

datetime2 = datetime1
datetime2 += datetime.timedelta(seconds=2)
print("datetime1", datetime1)
print("datetime2", datetime2)
