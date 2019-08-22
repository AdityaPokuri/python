class onec():
    def func():
        a=8
        b=9
        return a+b
 
	
    def __new__(self):
        return self
 
def func2(x,y):
    c=onec().func() 
 
    z=x+y+c
    return z
