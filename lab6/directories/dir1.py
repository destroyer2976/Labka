import os
def specific(path):
    directories = [smth for smth in os.listdir(path) if os.path.isdir(smth) ]
    files = [smth for smth in os.listdir(path) if os.path.isfile(smth)]
    return directories,files
def everything(path):
    alldir=[]
    allfiles=[]
    
    w=os.walk(path)
    for(p,d,f) in w:
        alldir.extend(d)
        allfiles.extend(f)
        return alldir,allfiles
    
link='C:\\Users\\user\\Desktop\\githowto\\repositories\\lab4'

directories,files=specific(link)
print("specific directories are" , directories)
print("specific files are", files)
alldir,allfiles=everything(link)
print("all directories are", alldir)
print("all files are", allfiles)