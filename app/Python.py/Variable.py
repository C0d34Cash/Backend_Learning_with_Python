# Variable = A name that stores a value in memory. Like a box with a label.
# Variable Name ->  Box  -> Value Inside
# name          ->  [   ] -> "Debojyoti"
# Rules in Python:
# Must start with letter or _ : name, _age ✅ | 1name ❌
# No spaces : my name ❌ | my_name ✅
# Case-sensitive : Age and age are different
# You can change it:
# pythonx = 10
# x = 20 
# # now x is 20
# That's it.

a = 10
b = 20
print(a + b) # 30

id(a) # This will return the memory address of the variable a
print(id(a)) # This will print the memory address of the variable a


# GARBAGE COLLECTION (GC) 
# Garbage Collection (GC) = Python automatically cleaning up memory you no longer use.
# Example:
x = [1, 2, 3]  # Python reserves memory for this list
x = None       # Now [1,2,3] has no variable pointing to it = garbage
# Python's GC will automatically delete it and free the memory

# How it works:
# You create variable -> Python gives it memory
# You delete / re-assign / function ends -> No one uses that memory anymore
# GC comes and deletes it -> Memory becomes free for other programs

a = "My fav language is Python!"
b = "My fav language is Python!"
print(id(a)) # This will print the memory address of the variable a
print(id(b)) # This will print the memory address of the variable b





# String Interning = Python saving memory by re-using the same string object instead of making 2 copies.

# Code 1: Auto Interning (small strings)
a = "hello"
b = "hello"

print(id(a))
print(id(b))
print(a is b) # True -> Same memory! InternedPython thought: hello is small & simple, let's reuse.

# Code 2: Not Interned (long / with symbols)

a = "My fav language is Python!"
b = "My fav language is Python!"

print(a is b) # False -> Different memory
print(a == b) # True -> Value same, but house differentSpace and ! breaks auto-interning.

# Code 3: Force Interning
# You can force it with sys.intern()

import sys
a = sys.intern("My fav language is Python!")
b = sys.intern("My fav language is Python!")

print(a is b) # Now True! You forced optimization
print(id(a) == id(b)) # True


# Code 4: The Real Proof 

import sys
# Without intern - 2 separate boxes
a = "Hello World! " * 100
b = "Hello World! " * 100
print(a is b) # False

# With intern - 1 box shared
a = sys.intern("Hello World! " * 100)
b = sys.intern("Hello World! " * 100)
print(a is b) # True - Saves lots of RAM

# Summary: == checks value: a == b; is checks memory: a is b; Interning = making is True to save memory










# OPTIMIZATION LIMITS

# From your last code, Python re-uses memory for a and b to save RAM. But it has limits.

# 1. String Interning LimitPython auto-optimizes ONLY simple strings.
a = "hello"
b = "hello"
print(a is b) # True -> Optimized

a = "My fav language is Python!"
b = "My fav language is Python!"
print(a is b) # False in many cases -> Too long / has space & symbols, Python says "too risky to optimize"

# Rule: If string has space, !, long length, Python often does NOT optimize.2. Integer Limit (-5 to 256)
a = 100
b = 100
print(a is b) # True -> Optimized (small int)

a = 1000
b = 1000
print(a is b) # False -> Not optimized (big int, limit crossed)

# Python pre-saves only -5 to 256 in memory.

# 3. Why Limits?
# If Python tried to check EVERY big string / big number to see if it already exists, your program would become very slow.
# So it says:"I will optimize only small, common things. For big things, I will just create new memory. 
# Speed > Saving a little RAM.
# "That's optimization limits.



# PRACTICE PROBLEM

a = "telusko"
b = "telusko"
print(a is b) # True -> Optimized
print(id(a) == id(b)) # True -> Same memory
print(a == b) # True -> Same value
print(a is not b) # False -> Same memory
print(a != b) # False -> Same value
print(a is b and a == b) # True -> Same memory & value
print(a is not b or a != b) # False -> Same memory & value
print(a is b or a != b) # True -> Same memory & value
