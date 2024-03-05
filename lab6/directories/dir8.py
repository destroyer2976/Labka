import os

file="C:\\Users\\user\\Desktop\\githowto\\repositories\\lab6\\directories\\prob.py"

def deletor(f):

    if not os.path.exists(f):
        print("path does not exist")
    else:
        if not os.access(f, os.X_OK):
            print("you do not have access to this file")
        else:
            os.remove(f)
            print("you have successfully deleted the file")
deletor(file)