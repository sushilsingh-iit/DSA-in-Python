#types of inheritance 
# single level inheritance 
# multi level inheritance 
# Hierarchical Inheritance

#1. Single Inheritance


class Parent:
    def func1(self):
        print("Parent function")

class Child(Parent):
    def func2(self):
        print("Child function")

obj = Child()
obj.func1()  # Access Parent
obj.func2()  # Access Child

# 2. Multi-level InheritanceGrandparent 
# Parent Child chain of inheritance where a child inherits from a parent,
# who inherited from another class.

class Grandparent:
    def func1(self):
        print("Grandparent")

class Parent(Grandparent):
    def func2(self):
        print("Parent")

class Child(Parent):
    def func3(self):
        print("Child")

obj = Child()
obj.func1()  # Access Grandparent
obj.func2()  # Access Parent
obj.func3()  # Access Child



# 3. Hierarchical InheritanceOne
# Parent  Many Children Multiple different child classes
# inherit from the same single parent class.


class Parent:
    def func1(self):
        print("Parent function")

class Child1(Parent):
    def func2(self):
        print("Child 1 function")

class Child2(Parent):
    def func3(self):
        print("Child 2 function")

c1 = Child1()
c2 = Child2()

c1.func1()  # Child 1 accesses Parent
c2.func1()  # Child 2 accesses same Parent




