# 1. Basic Usage

# You can print strings, numbers, or variables directly.
# Python

# name = "Alice"
# age = 25

# print(name)      # Output: Alice
# print(100)       # Output: 100

# 2. Printing Multiple Items

# You can print multiple items at once by separating them with commas. Python will automatically insert a space between them.
# Python

# print("My name is", name, "and I am", age)
# # Output: My name is Alice and I am 25

# 3. Customizing the Separator (sep)

# By default, Python separates items with a space. You can change this using the sep parameter.
# Python

# print("apple", "banana", "cherry", sep="-")
# # Output: apple-banana-cherry

# print("user", "domain.com", sep="@")
# # Output: user@domain.com

# 4. Customizing the End Character (end)

# By default, Python adds a new line (\n) after every print statement, which is why the next print command starts on a new line. You can change this behavior using the end parameter.
# Python

# print("Hello", end=" ")
# print("World")
# # Output: Hello World (on a single line)

# 5. Formatting Variables (f-strings)

# The most modern and readable way to insert variables into a print statement is using f-strings (formatted string literals). You put an f before the quotes and wrap variables in curly braces {}.
# Python

# item = "Coffee"
# price = 5.50

# # The old way (comma separation)
# print("The price of", item, "is", price)

# # The modern way (f-string)
# print(f"The price of {item} is ${price}")
# # Output: The price of Coffee is $5.50

# Summary Table of Parameters

# The formal syntax is print(object(s), sep=' ', end='\n').
# Parameter	Default Value	Description
# objects	N/A	The values you want to print (strings, numbers, etc.).
# sep	' ' (Space)	What to put between multiple objects.
# end	'\n' (New Line)	What to print after the last object.