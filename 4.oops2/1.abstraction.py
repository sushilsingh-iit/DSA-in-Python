#abstractiobn - providing olny impt details 
# hide unnessesry details 
# 

# advantage - easy for customer 
# protect provide internal infomation to be leaked - addition security 



# abstract class - can not be initialiaz  mean can not create object 
# at leat one abstract method  

# abstract class me abc is a inbuild module hota hai 

class animal :
    def eat (self):
        pass 

Animal = animal ()  # no use 
Animal.eat()

# lets create  a  abstarct method 

from abc import ABC , abstractmethod


# class animal (ABC):
#     @abstractmethod
#     def eat (self):
#         pass 
# a = animal ()   # not runing code 

class dog (animal):
    def sleep (self):
        print("dog is sleeping ")
    def eat(self):
        print("dog is eating ")

d = dog()

# both parent and child same method then call overwriting 