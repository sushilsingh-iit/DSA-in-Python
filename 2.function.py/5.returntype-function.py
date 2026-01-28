def add_number(a: int ,b : int ) -> int :  # int type of return 
    return a+b

print(add_number(2.5,1))
print(type(add_number))

#that is impeleset conversion

# function nesting
def outer_fun():
    print("hello from the outer ")

    def inner():
        print("hello from the inner")

    return inner

fn = outer_fun()
fn() 
outer_fun()() # both run same time 