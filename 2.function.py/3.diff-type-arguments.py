# default argument 

def greed(name ,massage="good morning"):  # default arguments 
    print(name,massage)
    

greed("sushil" , "hello")
greed("sushil")
# key word arguments

def dree(name ,age ,message):
    print(message,name,"your age is ",age)

dree(name="suhsil",age=21,message="hello")
print(dree)

# positional argument 
def add_number(x,y):
    print("x " , x)
    print("y ", y)
    print(x+y)

add_number(5,6)



