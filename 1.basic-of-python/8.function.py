# A function in Python is a reusable block of code that performs a specific task.

# Instead of writing the same code over and over again, you wrap it inside a function and "call" it whenever you need it. This keeps your code organized, readable, and efficient (following the DRY principle: Don't Repeat Yourself).

# Here is a breakdown of how functions work in Python.
# 1. Defining and Calling a Function

# You create a function using the def keyword.

#     Define: Write the code once.

#     Call: Execute the code by using the function's name followed by parentheses ().

# Python

# # 1. Definition
# def greet():
#     print("Hello! Welcome to Python.")

# # 2. Call
# greet() 
# # Output: Hello! Welcome to Python.

# 2. Parameters and Arguments

# Functions become much more powerful when you pass data into them.

#     Parameter: The variable listed inside the parentheses in the function definition.

#     Argument: The actual value you send to the function when you call it.

# Python

# def greet_person(name):  # 'name' is the parameter
#     print(f"Hello, {name}!")

# greet_person("Alice")    # "Alice" is the argument
# greet_person("Bob")

# 3. The return Statement

# Often, you don't just want a function to print something; you want it to calculate a value and send it back to you so you can store it in a variable. This is what return does.

#     Crucial Concept: print just shows text on the screen. return gives the value back to the code.

# Python

# def square(number):
#     return number * number

# # We capture the returned value in a variable
# result = square(4)
# print(result) # Output: 16

# # We can use the result immediately in math
# print(square(5) + 10) # Output: 35 (25 + 10)

# 4. Advanced Function Features
# Default Arguments

# You can provide a default value for a parameter. If the user calls the function without that argument, it uses the default.
# Python

# def greet(name="User"):
#     print(f"Hi, {name}.")

# greet("Alice") # Output: Hi, Alice.
# greet()        # Output: Hi, User.

# Arbitrary Arguments (*args)

# If you don't know how many arguments will be passed, add a * before the parameter name. Python will treat the arguments as a tuple.
# Python

# def sum_all(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total

# print(sum_all(1, 2, 3, 4)) # Output: 10

# Keyword Arguments (kwargs)

# You can also pass arguments using key=value syntax so the order doesn't matter.
# Python

# def describe_pet(animal, name):
#     print(f"I have a {animal} named {name}.")

# describe_pet(name="Harry", animal="Hamster")
# # Output: I have a Hamster named Harry.

# 5. Lambda Functions (Anonymous Functions)

# For very short, one-line functions, Python offers a shortcut called lambda.

#     Syntax: lambda arguments : expression

# Python

# # Regular function
# def add(x, y):
#     return x + y

# # Equivalent Lambda function
# add_lambda = lambda x, y : x + y

# print(add_lambda(5, 3)) # Output: 8