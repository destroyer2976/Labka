num=int(input("enterr"))
def fka(n):
    for i in range(0,n):
        if i%3==0 and i%4==0:
            yield i
            
generator=fka(num)

for kia in generator:
    print(kia)            