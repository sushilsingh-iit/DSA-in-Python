#advantage 
#1.reuse the code 
#2relationship  



#super keyword 

#access the parent properties 

class parent :
    property = 90 

class child(parent):
    property = 99
    
    def Display(self):
        print("child property " , self.property)
        print("parent property ", super().property)


obj = child()
obj.Display()