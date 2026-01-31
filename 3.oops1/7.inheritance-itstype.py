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