a = 5
b = 6
# Variable swapping
c = a
a = b
b = c
print("a:",a)
print("b:",b)

# Mathematical swapping
a = a+b
b = a - b
a = a - b
print("a:",a)
print("b:",b)


# Bitwise XOR SwapIt swaps 2 numbers WITHOUT using a 3rd variable, using XOR ^ operator.
# XOR rule: Same = 0 (1 ^ 1 = 0)Different = 1 (1 ^ 0 = 1)How it works with a = 5, b = 10.
a = 5   # 0101 in binary
b = 10  # 1010 in binary

a = a ^ b  # a = 0101 ^ 1010 = 1111 = 15
b = a ^ b  # b = 1111 ^ 1010 = 0101 = 5 (original a)
a = a ^ b  # a = 1111 ^ 0101 = 1010 = 10 (original b)

print(a, b) # 10, 5 -> Swapped!



# Pythonic Swapping Method
a = 5
b = 10

a, b = b, a

print(a) # 10

a = 5
b = 6
# Variable swapping
c = a
a = b
b = c
print("a:",a)
print("b:",b)

# Mathematical swapping
a = a+b
b = a - b
a = a - b
print("a:",a)
print("b:",b)


# Bitwise XOR SwapIt swaps 2 numbers WITHOUT using a 3rd variable, using XOR ^ operator.
# XOR rule: Same = 0 (1 ^ 1 = 0)Different = 1 (1 ^ 0 = 1)How it works with a = 5, b = 10.
a = 5   # 0101 in binary
b = 10  # 1010 in binary

a = a ^ b  # a = 0101 ^ 1010 = 1111 = 15
b = a ^ b  # b = 1111 ^ 1010 = 0101 = 5 (original a)
a = a ^ b  # a = 1111 ^ 0101 = 1010 = 10 (original b)

print(a, b) # 10, 5 -> Swapped!



# Pythonic Swapping Method
a = 5
b = 10

a, b = b, a

print(a) # 10
print(b) # 5

# Why it works? - 
# Tuple UnpackingPython does it in 2 steps internally:
# Step 1: Right side creates a tuple
temp_tuple = (b, a) # (10, 5)

# Step 2: Left side unpacks it
a = temp_tuple[0] # 10
b = temp_tuple[1] # 5
# You can see it:
a = 5
b = 10

print((b, a)) # (10, 5) -> This is a tuple

a, b = (b, a) # Unpacking, brackets are optional

# More pythonic ways
# 3 variables
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c) # 2 3 1

# List elements
nums = [1, 2, 3, 4]
nums[0], nums[3] = nums[3], nums[0]
print(nums) # [4, 2, 3, 1]

# In a loop - reverse string
s = list("hello")
s[0], s[4] = s[4], s[0]
print("".join(s)) # oellh

# This is the only swap method you should use in your Backend project.
# It's fast, clean, and every Python developer understands it.
# The other methods (temp variable, XOR, + -) are just for learning.


# PRACTICE PROBLEM
str1 = "Debojyoti"
str2 = "Telusko"
str1, str2 = str2, str1
print("str1:",str1)
print("str2:",str2)