import math
numsides=int(input('enter number of sides'))
lengthside=int(input('enter lenght of one side'))
def area(n,l):
    angle=180/n
    rad=math.radians(angle)
    tangle=math.tan(rad)
    apothem=l/(2* tangle)
    Ar=(n*l*apothem)/2
    print(Ar)
    
area(numsides, lengthside)


# import math
# len=25
# num=4
# Area=len**2
# print(Area)