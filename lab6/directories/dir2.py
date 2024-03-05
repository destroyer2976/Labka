import os
def access(path):
    if not os.path.exists(path):
        print("Path doesnt exist")
        return
    if not os.access(path, os.R_OK):
        print("path is not readable")
    else:
        print("path is readable")
    if os.access(path, os.W_OK):
        print("path is writtable")
    else:
        print("path is not writtable")
    if os.access(path, os.X_OK):
        print("path is executable")
    else:
        print("path is not executable")
        
link='C:\\Users\\user\\Desktop\\githowto\\repositories\\lab4'
access(link)
    
    
    
