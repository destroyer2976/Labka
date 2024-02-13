num=[4,3,2,1]
def histog(list):
    maxstars=10
    for x in range(len(num)):
        remstars=maxstars-num[x]
        print(num[x]*" ", end="") 
        print( "*"*remstars)
    
   
    
histog(num)
    