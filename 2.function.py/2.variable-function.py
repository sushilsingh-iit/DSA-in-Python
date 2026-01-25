s = 202 # globle varibale/ globle scope 
def funct():
    s = 202 # local scope variable
    print(s)

funct()
print(s)


