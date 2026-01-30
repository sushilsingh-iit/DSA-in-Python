#encapsulation
# Encapsulation is one of the fundamental concepts in Object-Oriented Programming (OOP).
# It describes the idea of bundling data (variables) and methods (functions) that work on that data within one unit, like a class.


class person :
    def __init__(self,name ,car):
        self.__name = name 
        self.__car = car 
        
# second part of encaplsulation


#getter and setter - public method to allow the controlled interaction

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    def get_car(self):
        return self.__car
    def set_car(self , car):
        self.__car = car


per = person("sushil", 21)
print(per.get_name())
per.set_name("singh ji ")
print(per.get_name())
