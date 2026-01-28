#kwargs in python


def display_info(**kwarys):
    print(kwarys)
    print(type(kwarys))

    for key , value in kwarys.items():
        print(key, "->" , value)

display_info(name="sushil",age=21,city="bagalore")


def func ( a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


func(5,4,3,2,1,0 , name="sushil",age=21)

# kwargs is always last parameter

