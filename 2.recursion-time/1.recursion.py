def factorial(n):
    # Base Case: The factorial of 1 is 1.
    if n == 1:
        return 1
    
    # Recursive Case: 5 * factorial(4)
    else:
        return n * factorial(n - 1)

print(factorial(1)) # Output: 120