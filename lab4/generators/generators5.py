num=int(input("enter"))
def down(n):
    
    for i in range(n,-1,-1):
        yield i
        
generator=down(num)

for u in generator:
    print(u)  