#single inheritance 

# class animal :
#     def __init__(self,name):
#         self.name = name 

#     def eat (self):
#         print ( "animal is eating ")
# class Dog(animal):
#     def __init__(self, name ,type):
#         super().__init__(name)
#         self.type = type 


#multi level iheritance 


class animal :
    def __init__(self ,name):
        self.name = name

    def eat(self):
        print("animal is eating ")

class Dog(animal):
    def __init__(self, name , type ):
     super().__init__(name)
     self.type = type 


class Pet (Dog):
    def __init__(self,name,type,houseName):
        super().__init__(name ,type)
        self.houseName = houseName




 


