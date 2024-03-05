import os
def name(path):
    if os.path.exists(path):
        print(os.path.dirname(path))
        print(os.path.basename(path))
    else:
        print("path doesnt exist")
        
link='C:\\Users\\user\\Desktop\\githowto\\repositories\\lab4'
name(link)