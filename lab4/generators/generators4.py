num1=int(input('enter start'))
num2=int(input('enter finish'))
def squares(n,m):
    for i in range(n,m+1):
        yield i**2

generator=squares(num1,num2)

for sq in generator:
    print(sq)