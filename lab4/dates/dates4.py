import datetime
today=datetime.datetime.now()
other=datetime.timedelta(days=1)
new=today-other
diff=(today-new).total_seconds()

print('difference in sceonds is',diff)







# from datetime import datetime

# date1_str = input("Enter 1 date (format: YYYY-MM-DD): ")

# date2_str = input("Enter 2 date (format: YYYY-MM-DD): ")

# date1 = datetime.strptime(date1_str, "%Y-%m-%d")
# date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# difference=date2-date1
# sec=difference.total_seconds()

# print(sec)