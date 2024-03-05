
def aaa(f):
    listtof=[1, 2, 3]

    with open(f, "a") as file:
        file.write(", ".join(str(i) for i in listtof))


def bbb(f):
    with open(f, "r") as file:
        print(file.read())


filename='C:\\Users\\user\\Desktop\\githowto\\repositories\\lab6\\directories\\demo.txt'

aaa(filename)

bbb(filename)