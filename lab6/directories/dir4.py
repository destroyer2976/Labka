
def lines(fil):
    with open(fil) as file:
        san=0
        for line in file:
            san+=1
    return san
    
filename='C:\\Users\\user\\Desktop\\githowto\\repositories\\lab6\\directories\\demo.txt'
print("number of lines", lines(filename))
            
