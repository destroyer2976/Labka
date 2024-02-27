import re
with open('row.txt', 'r', encoding='utf-8') as file:
    check=file.read()
    mylist=[]
    need=check.split()
    for i in need:
        find=re.search(r'[A-Z].[a-z]+', i)
        if find:
            mylist.append(i)
            
print(mylist)

                