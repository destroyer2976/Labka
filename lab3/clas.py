class Ty:
    def __init__(self,par):
        self.par=par
        
class Son(Ty):
    def __init__(self,par,par1):
        super().__init__(par)
        self.par1=par1
        
        
opp=Son(3,4)
print(opp.par, )
    
