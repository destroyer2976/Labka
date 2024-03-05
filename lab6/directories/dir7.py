def bbb(f):
    with open(f, "r") as file:
        bll=file.read()

    newf="newf.txt"

    with open(newf, "w") as file:
        file.write(bll)

bbb('C:\\Users\\user\\Desktop\\githowto\\repositories\\lab6\\directories\\demo.txt')