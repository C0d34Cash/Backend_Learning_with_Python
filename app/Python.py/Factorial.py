# INTRODUCTION - What is Factorial?
# Factorial is written as n! 
# It means you multiply a number by every number below it down to 1.Real life example: How many ways can you arrange 3 books?
# 3! = 3 x 2 x 1 = 6 ways.Rule: 0! = 1 - This is defined by math, remember it.

# UNDERSTANDING THE MATH
# 1! = 1
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# Pattern: n! = n _ (n-1)!
# So 5! = 5 _ 4! - This is why recursion works.
# Growth is very fast: 10! = 36,28,800 and 20! is already 19 digits long.

# SETTING UP THE CODE
# We need 3 things before coding:
# Input n - non-negative integer
# Edge case - if n < 0, error. If n = 0, answer 1.
# Variable result = 1 to store multiplication.Create file factorial.py

# Basic setup
n = int(input("Enter n: "))

if n < 0:
    print("Factorial not defined for negative numbers")
elif n == 0:
    print("Factorial is 1")

#  IMPLEMENTING THE LOGIC
# Method A - Iterative (Best for interviews - No stack overflow):
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = int(input("Enter n: "))
print(f"{n}! = {factorial_iterative(n)}")

# Method B - Recursive (Clean but risky for large n):
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)
n = int(input("Enter n: "))
print(f"{n}! = {factorial_iterative(n)}")

# Final Complete Code:
def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5)) # 120
