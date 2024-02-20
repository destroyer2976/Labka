import datetime
today=datetime.date.today()
diff=datetime.timedelta(days=5)
result=today-diff
print('today is ', today)
print('new dateis', result)
