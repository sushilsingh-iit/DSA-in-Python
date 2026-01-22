# 1. Numeric Types

# Used to store numbers.
# Data Type	Description	Example
# int	Whole numbers (integers), positive or negative, without decimals.	x = 10
# float	Numbers containing a decimal point.	y = 3.14
# complex	Numbers with a real and an imaginary part (written with j).	z = 1 + 2j
# 2. Text Type

# Used to store text or characters.

#     str (String): A sequence of characters enclosed in single '...' or double "..." quotes.

#         Example: name = "Python"

# 3. Boolean Type

# Used to represent truth values, essential for conditional logic.

#     bool: Can only hold one of two values: True or False.

#         Example: is_learning = True

# 4. Sequence Types

# Used to store multiple values in an ordered sequence.
# Data Type	Description	Example	Mutable? (Can be changed?)
# list	An ordered collection of items.	fruits = ["apple", "banana"]	Yes
# tuple	An ordered collection of items, similar to a list but immutable.	coordinates = (10, 20)	No
# range	Generates a sequence of numbers, often used in loops.	numbers = range(5)	No
# 5. Mapping Type

# Used to store data in "key:value" pairs.

#     dict (Dictionary): Extremely fast for looking up data. Keys must be unique.

#         Example: person = {"name": "Alice", "age": 21}

# 6. Set Types

# Used to store collections of unique, unordered items.

#     set: Great for mathematical operations like finding intersections or removing duplicates from a list.

#         Example: unique_numbers = {1, 2, 3, 3, 4} (duplicates are ignored, resulting in {1, 2, 3, 4})

# 7. None Type

# Used to define a null value or the absence of a value.

#     NoneType: It is not the same as 0 or an empty string; it literally means "nothing".

#         Example: result = None

# How to Check a Data Type

# If you are ever unsure what data type a variable is holding, you can use the built-in type() function:
# Python

# x = 10.5
# print(type(x))  # Output: <class 'float'>

# y = "Hello"
# print(type(y))  # Output: <class 'str'>

#     Note on Casting: You can change data types using constructor functions. For example, int("10") converts a string to an integer, and str(50) converts an integer to a string.