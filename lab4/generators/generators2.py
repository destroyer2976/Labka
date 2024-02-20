num=int(input("Babe, Enter) "))
def da(n):
    for i in range(0,n,2):
        yield (i)
        
listik=list(da(num))

for evens in listik:
    print(evens, end=",")