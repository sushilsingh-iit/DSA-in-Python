
#implicit method overloading 

class calculator :
    # def __init__(self,a ,b ):   # you can not overload 
    #     return a + b 
    def add(self ,a,b,c=0):
        return a+b+c
    
cal = calculator()

print(cal.add(5,6,7))