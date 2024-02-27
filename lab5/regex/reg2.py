import re
with open('row.txt', 'r', encoding='utf-8') as file:
    data=file.read()
    listik=[]
    kiara=data.split()
    for i in kiara:
        g=re.search(r'a.{2,3}b',i)
        if g:
            listik.append(i)
            
print(listik)
    