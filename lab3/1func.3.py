heads=int(input('enter heads'))
legs=int(input("enter legs"))

def solve():
    rab=int((legs-2*heads)/2)
    chic=int(heads-rab)
    print("rabbits number is", rab, "and chickens are" , chic)
    
solve()
    
   
