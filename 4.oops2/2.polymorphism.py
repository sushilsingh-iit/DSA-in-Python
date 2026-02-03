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

