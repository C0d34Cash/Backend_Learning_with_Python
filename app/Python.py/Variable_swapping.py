<<<<<<< HEAD
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
=======
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
>>>>>>> 4aafddda039d6c9eb15ed5038b39ef71a2559924
print(b) # 5