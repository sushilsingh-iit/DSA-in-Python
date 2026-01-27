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

# positational argument 
def add_number(x,y):
    print("x " , x)
    print("y ", y)
    print(x+y)

add_number(5,6)


def sum_number(*args):
    print(type(args))
    print(args)

    sum = 0
    for num in args : 
        sum +=num 
    return sum 

print(sum_number(1,2,3,4,5))

