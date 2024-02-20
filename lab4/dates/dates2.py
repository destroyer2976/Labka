import datetime
diff=datetime.timedelta(days=1)
today=datetime.date.today()
tomo=today+diff
yest=today-diff
print('Yesterday was' , yest)
print('Today is', today)
print('Tomorrow will be', tomo)
