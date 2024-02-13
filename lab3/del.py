str=input("enter a string: ").split()


i=len(str)-1

newstr=[]
while i>=0:
    newstr.append(str[i])
    i-=1
    
print(*newstr)
    
