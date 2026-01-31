#inheritance 
#parent child relationship 

# gp - parent - you - child
# 1. The Parent Class


class Vehicle:
    def start(self):
        print("Vehicle started.")

# 2. The Child Class
class Car(Vehicle):  # The (Vehicle) tells Python to inherit
    def honk(self):
        print("Honk honk!")

# --- Usage ---

my_car = Car()

# The car can use the Parent's method
my_car.start()  # Output: Vehicle started.

# The car can use its own method
my_car.honk()   # Output: Honk honk!


class Animal:
    def __init__(self, name):
        self.name = name 

    def eat(self):
        print(self.name + " is eating.")

class Dog(Animal):
    def __init__(self, name, breed): 
        # "super()" is the modern way to call the parent class
        super().__init__(name)
        self.breed = breed

# 1. Create the instance (variable is usually lowercase)
my_dog = Dog("Seru", "Doberman")

# 2. Call the method on the instance
my_dog.eat()
