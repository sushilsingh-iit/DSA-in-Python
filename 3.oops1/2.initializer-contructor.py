class person :
    name = "sushil"
    age = 21

per1 = person()
per2 = person()
per3 = person()

print(per1.name)
print(per2.name)   # every one have same name 
print(per3.name)


class Person:
    #initializer / contructor for object
    def __init__(self,name,age):
        self.name = name  # initializing the state of the object 
        self.age = age 

per = Person("sushil",21)
per1 =Person("Singh", 22)
print(per.name)
print(per1.name)


class per:
    country = "india"
    def __init__(self,name,age):
        self.name = name 
        self.age = age

per7 = per("singhji",00)
per8 = per ("shivaji",00)

print(per7.name,per7.country,per7.age)
print(per8.name)
        