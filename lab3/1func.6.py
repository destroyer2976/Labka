
st=input("enter a string: ")

def rev(s):

    newSt=""  

    ind=len(s)-1  

    while ind>=0:

        endInd=ind 
        while ind>=0 and s[ind]!=" ":
            ind-=1  

        newSt+=s[ind+1:endInd+1]+" " 
        ind-=1  

    print(newSt)

rev(st)