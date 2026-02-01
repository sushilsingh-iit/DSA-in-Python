#advantage 
#1.reuse the code 
#2relationship  



#super keyword 

#access the parent properties 

class parent :
    property = 90 

    def eat(self):
        print("parent eating")  #

class child(parent):
    property = 99
    
    def Display(self):
        print("child property " , self.property)
        print("parent property ", super().property)

    def eat(self):
        print("child eating")  #     # method over writing 


    def calleat(self):
        self.eat()   # this is representing is child 
        super().eat() #this is represent is parent 



obj = child()
obj.Display()