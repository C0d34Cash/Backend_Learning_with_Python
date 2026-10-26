#  INTRODUCTION - What is Recursion?
# Recursion is when a function calls itself.
# Think of Russian dolls. 
# To open the big doll, you need to open the smaller one inside, and so on.
# It has 2 parts - 
# MANDATORY:Base Case: When to STOP (otherwise infinite)
# Recursive Case: Call itself with a smaller problem

# Example - Factorial:
n = int(input("Take your n: "))
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case - smaller problem n-1
    return n * factorial(n-1)
n = int(input("Take your n: "))
print(factorial(n))
# Flow for factorial(3):
# 3 _ factorial(2) -> 3 _ 2 _ factorial(1) -> 3 _ 2 * 1 = 6

# INFINITE LOOPS - The Biggest Mistake
# If you forget the Base Case, recursion never stops.
# Wrong Code:
# def bad_recursion(n):
#    print(n)
#    return bad_recursion(n-1) # Where to stop? Never! 

# bad_recursion(5) # 5, 4, 3, 2, 1, 0, -1, -2... forever

# Python will stop it and throw: RecursionError: maximum recursion depth exceeded
# This is like a while True: loop with no break. 
# Every call takes memory (stack).
# Infinite calls = Memory full = Crash.
# Rule: Always write Base Case FIRST.

def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}-> Calling factorial({n})")

    if n == 0 or n == 1:
        print(f"{indent}<- Base case reached, returning 1")
        return 1

    result = n * factorial(n-1, depth+1)
    
    print(f"{indent}<- Returning from factorial({n}) = {result}")
    return result

factorial(4)


# PRACTICE PROBLEM
def print_numbers(n):
    # Base Case: when to stop
    if n > 5:
        return
    
    # Work: print current number
    print(n)
    
    # Recursive Case: call for next number
    print_numbers(n + 1)

# Start from 1
print_numbers(1)
