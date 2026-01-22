# arithmetic operators:
# used fro mathmetical calculations.
# 1. Arithmetic Operators

# Used for standard mathematical operations.


# Operator	Name	Example (a = 10, b = 3)	Result
# +	Addition	a + b	13
# -	Subtraction	a - b	7
# *	Multiplication	a * b	30
# /	Division (Float)	a / b	3.333...
# //	Floor Division	a // b	3 (Rounds down to nearest whole number)
# %	Modulus	a % b	1 (Returns the remainder)
# **	Exponentiation	a ** b	1000 (10 to the power of 3)



# 2. Comparison (Relational) Operators

# Used to compare two values. They always return a Boolean value (True or False).
# Operator	Name	Example (a = 10, b = 3)	Result
# ==	Equal to	a == b	False
# !=	Not equal to	a != b	True
# >	Greater than	a > b	True
# <	Less than	a < b	False
# >=	Greater than or equal to	a >= b	True
# <=	Less than or equal to	a <= b	False



# 3. Logical Operators

# Used to combine conditional statements.
# Operator	Description	Example
# and	Returns True if both statements are true	(5 > 3) and (10 < 20) is True
# or	Returns True if one of the statements is true	(5 > 3) or (10 > 20) is True
# not	Reverses the result (returns False if the result is True)	not(5 > 3) is False



# 4. Assignment Operators

# Used to assign values to variables.

#     = (Simple Assignment): x = 5

#     Compound Assignment: Performs an operation and assigns the result back to the variable.

#         x += 3 is the same as x = x + 3

#         x -= 3 is the same as x = x - 3

#         x *= 3 is the same as x = x * 3




# 5. Membership Operators

# Used to test if a sequence (like a string, list, or tuple) contains a specific object.

#     in: Returns True if the value is present.

#         'a' in 'apple' -> True

#     not in: Returns True if the value is not present.

#         'z' not in 'apple' -> True



# 6. Identity Operators

# Used to compare the memory locations of two objects, not just if they are equal, but if they are actually the exact same object.

#     is: Returns True if both variables point to the same object.

#     is not: Returns True if both variables point to different objects.

# Python

# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x

# print(x == y) # True (they have the same values)
# print(x is y) # False (they are different lists in memory)
# print(x is z) # True (z is exactly the same object as x)




# 7. Bitwise Operators

# Used to compare binary numbers (generally used in more advanced programming, cryptography, and systems programming).

#     & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift).

# 💡 Pro Tip: Operator Precedence

# Just like BODMAS in mathematics, Python follows an order of operations. Exponentiation (**) happens first, followed by Multiplication/Division (*, /, //, %), and finally Addition/Subtraction (+, -). You can always use parentheses () to force Python to evaluate a specific part of an expression first.

# Would you like to see some coding examples of how to use these in an if/else statement, or practice with a specific operator?