import re
with open('row.txt','r', encoding='utf-8') as file:
    infa=file.read()
    matches=re.findall(r'[a-z]+_[a-z]+', infa)
    
    for match in matches:
      print(match)
        
    
    