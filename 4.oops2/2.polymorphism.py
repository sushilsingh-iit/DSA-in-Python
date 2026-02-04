#polymorphism 


class animal :
    def eat (self):
        print("animal is eating ")

class dog(animal):
    def eat(self): # method overrinding 
        print("dog is eating ")

class cat(animal) :
    def eat(self): # method overriding 
        print("cat is eating ")



c = cat()
d = dog()
a = animal()

c.eat()
d.eat()
a.eat()



# polymorphism is using inheritance 


class BirdFly :
    def flyBird (self,bird):  # i need to have bird object 
        bird.fly ()
class Parrot :
    def fly (self):
        print("parrot is flying ")

class Crow :
    def fly(self):
        print("Crow is flying ")

p = Parrot()
c = Crow()

bf = BirdFly()
bf.flyBird(p)
bf.flyBird(c)