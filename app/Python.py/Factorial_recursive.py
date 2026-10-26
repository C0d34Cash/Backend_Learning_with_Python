# Let's take factorial(4) as example.
# 1. RECURSIVE LOGICThe math formula is:
# n! = n * (n-1)!To get 4!, you need 3!
# To get 3!, you need 2!
# To get 2!, you need 1!So we break a big problem into a smaller same problem.
def factorial(n):
    return n * factorial(n-1)  # same function, smaller n
# But this alone will go infinite. So we need a stop.

# 2. BASE CASE AND RETURN
# Base Case: if n == 0 or n == 1: return 1
# Why? Because 1! = 1 and 0! = 1 is defined.
# This is where recursion STOPS and starts returning.Without it:
# 4 -> 3 -> 2 -> 1 -> 0 -> -1 -> -2... never ends = RecursionError
# With it: 4 -> 3 -> 2 -> 1 -> STOP, return 1

# 4. FUNCTION CALL STACK - What computer does
# Computer uses a Stack - Last In, First Out. Like plates.


# 6. CODE IMPLEMENTATION
def factorial(n):
    # 1. Base Case
    if n == 0 or n == 1:
        return 1
    
    # 2. Recursive Case + Return
    return n * factorial(n-1)

# Test
print(factorial(5)) # 24
print(factorial(10)) # 120

# With full debug prints for you:
def factorial_debug(n, depth=0):
    print("  "*depth + f"factorial({n}) called")
    if n <= 1:
        print("  "*depth + f"-> base case, returning 1")
        return 1
    result = n * factorial_debug(n-1, depth+1)
    print("  "*depth + f"-> factorial({n}) = {result}")
    return result

factorial_debug(6)




print("PRACTICE PROBLEM")
def fact(n):
    if n == 0:
        return 0
    return n * fact(n-1)
res = fact(4)
print(res)