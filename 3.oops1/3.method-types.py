#method are tree type - 
#instance method
#class method
#static method




#instance method
class person:
    def __init__(self,name,age ):
        self.name = name 
        self.age = age
    

    def find_age(self):
        return self.age
    
per = person("sushil",21)
print(per.find_age())



#class method 
class person:

    country = "india"

    @classmethod
    def greet(cls):
        print("Hello from the class", cls.country)  # access to the class fields No access to the object properties 

    def __init__(self,name,age ):
        self.name = name 
        self.age = age
    

    def find_age(self):
        return self.age
    
per = person("sushil", 22)
print(per.find_age())

person.greet()


# # class and object both 
# no access to object property
# access to the class



# satatic method


#class method 
class person:

    country = "india"

    @classmethod
    def greet(cls):
        print("Hello from the class", cls.country)  # access to the class fields No access to the object properties 


    @staticmethod    # totaly indipendent
    def hello():
        print("hello")


    def __init__(self,name,age ):
        self.name = name 
        self.age = age
    

    def find_age(self):
        return self.age
    
per = person("sushil", 22)
print(per.find_age())

person.greet()
person.hello()
