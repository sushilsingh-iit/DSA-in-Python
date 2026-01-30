# public and private

class person :
    def __init__(self ,name , age, salary ):
        self.name = name 
        self.age = age 
        self.__salary = salary

    def findage(self):
        return self.age
    
    def get_salary(self):
        print(self.__salary) # This works because it is INSIDE the class
        self.__calculatetax()

    def __calculatetax(self):
        print("calculating tax")
    
per = person("sushil", 21, 2500) 

print(per.name)
per.get_salary() # output: 2500



        