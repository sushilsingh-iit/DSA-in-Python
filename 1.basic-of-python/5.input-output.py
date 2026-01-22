# 1. Standard Input: input()

# The input() function pauses your program and waits for the user to type something on the keyboard and press Enter.
# Basic Syntax

# You can put a string inside the parentheses to act as a prompt (a message telling the user what to type).
# Python

# name = input("What is your name? ")
# print(f"Nice to meet you, {name}!")




# 2. Standard Output: print()

# This sends data out to the screen. (We covered this in detail previously, but here is a quick recap of the most important style).

# Best Practice: Use f-strings to mix text and variables cleanly.
# Python

# score = 95
# print(f"Game Over. Final Score: {score}")





# 3. File Input and Output (File I/O)

# Sometimes "Input/Output" refers to reading from and writing to files on your computer, rather than talking to a user.

# To do this, we use the open() function.
# Writing to a File

# Use mode 'w' (Write). Note: This creates the file if it doesn't exist, or overwrites it if it does.
# Python

# # 'w' means Write mode
# with open("notes.txt", "w") as file:
#     file.write("This is line 1.\n")
#     file.write("This is line 2.")

# Note: Using with is recommended because it automatically saves and closes the file for you, even if an error occurs.
# Reading from a File

# Use mode 'r' (Read).
# Python

# # 'r' means Read mode
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)


