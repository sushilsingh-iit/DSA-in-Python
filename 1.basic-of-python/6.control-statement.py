# Control statements determine the order in which code is executed. They allow your program to make decisions, repeat actions, and jump between different sections of code.

# Without control statements, Python would just execute your code line-by-line from top to bottom.

# Here are the three main types of control statements in Python:
# 1. Conditional Statements (Decision Making)

# These allow the program to choose different paths based on whether a condition is True or False.

#     if: Executes code only if the condition is true.

#     elif (Else If): Checks a new condition if the previous if was false.

#     else: Executes code if none of the previous conditions were true.

# Python

# score = 75

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: F")





# 2. Looping Statements (Iteration)

# These are used to repeat a block of code multiple times.

# The for Loop

# Used when you want to iterate over a sequence (like a list, string, or range of numbers). You generally use this when you know how many times you want to loop.
# Python

# # Loop through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # Loop 5 times (0 to 4)
# for i in range(5):
#     print(f"Count: {i}")

# The while Loop

# Used to repeat code as long as a specific condition remains True. You generally use this when you don't know exactly when the loop will end (e.g., waiting for user input).

# Getty Images
# Python

# count = 5
# while count > 0:
#     print(count)
#     count -= 1  # Decrement count so the loop eventually ends
# print("Blastoff!")




# 3. Transfer Statements (Jumping)

# These keywords alter the loop's natural behavior.

#     break: Immediately terminates the loop entirely.

#     continue: Skips the current iteration and jumps back to the top of the loop for the next one.

#     pass: Does nothing. It is a placeholder used when syntax requires a line of code, but you don't want any command executed.

# Python

# for i in range(10):
#     if i == 3:
#         continue  # Skip printing 3
#     if i == 8:
#         break     # Stop the loop entirely when we reach 8
    
#     if i == 0:
#         pass      # Do nothing (just a placeholder)

#     print(i)

# Output of above: 0, 1, 2, 4, 5, 6, 7
# Summary Table
# Statement	Type	Function
# if / elif / else	Conditional	Decides which block of code to run.
# for	Loop	Repeats code for every item in a sequence.
# while	Loop	Repeats code while a condition is true.
# break	Transfer	Exits a loop immediately.
# continue	Transfer	Skips the rest of the current loop iteration.
# pass	Transfer	A null operation (placeholder).