import datetime
x=datetime.datetime.now()
newdat=x.replace(microsecond=0)
print('datetime with ms', x)
print('datetime without ms', newdat)