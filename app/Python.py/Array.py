# In Python we don't use "Array" much, we use List. 
# List = Python's array.

# LIMITATIONS OF LIST IN PYTHON:

# 1. Slow for math
a = [1,2,3]
b = [4,5,6]
# a + b = [1,2,3,4,5,6]  not [5,7,9] like you expect
# You can't do a * 2 = [1,2,3,1,2,3] not [2,4,6]

# 2. Uses more memory
# List stores different data types, so it stores extra info. 
# An array of 1 million ints in list takes ∼28MB, in NumPy takes ∼8MB.

# 3. Slow for large data
# Looping 1 crore elements in list is very slow vs NumPy which is written in C.

# 4. No type checking
arr = [1, 2, "hello", 3.5, True] # Everything allowed
# This causes bugs, you might accidentally put string in int list
# Real arrays allow only one type

# 5. No built-in matrix operations
# For 2D array you need nested lists [[1,2],[3,4]] which is messy. 
# No easy transpose, determinant etc.

# 6. Not good for fixed-size data
# If you know you always have 100 items, list still can grow/shrink, wasting checks.


# LIST THE ARRAY
# Create
arr = [10, 20, 30, 40, 50]

# Access - indexing starts at 0
print(arr[0])  # 10
print(arr[1])  # 20
print(arr[-1]) # 50 (last element)

# Change
arr[1] = 99
print(arr) # [10, 99, 30, 40, 50]


# LOOP THROUGH ARRAY
arr = [10, 20, 30, 40]

# for loop - most common
for num in arr:
    print(num)

# with index
for i in range(len(arr)):
    print(f"Index {i} = {arr[i]}")

# while loop (like you learned)
i = 0
while i < len(arr):
    print(arr[i])
    i += 1

# IMPORTANT LIST METHODS
arr = [1, 2, 3]

arr.append(4)      # add at end -> [1,2,3,4]
arr.insert(1, 99)  # insert at index 1 -> [1,99,2,3,4]
arr.pop()          # remove last -> [1,99,2,3]
arr.remove(99)     # remove value 99 -> [1,2,3]
len(arr)           # length = 3
sum(arr)           # sum = 6
max(arr)           # max = 3

# ============================================================================================
# ============================================================================================

# IMPORTING ARRAY MODULE
# This is the real array in Python (not list).
import array as arr
# or
import array
from array import array

# Full Example
import array as arr

# Syntax: array.array(typecode, [elements])

# typecodes:
# 'i' = signed integer
# 'f' = float
# 'd' = double float
# 'u' = unicode character

# Create integer array
my_array = arr.array('i', [10, 20, 30, 40, 50])

print(my_array)       # array('i', [10, 20, 30, 40, 50])
print(my_array[0])    # 10
print(my_array[2])    # 30

# Loop
for x in my_array:
    print(x)

# Methods - same as list mostly
my_array.append(60)
my_array.insert(1, 15)
print(my_array)  # array('i', [10, 15, 20, 30, 40, 50, 60])

# Type restriction - this will ERROR
# my_array.append("hello") -> TypeError
# my_array.append(3.5)     -> TypeError

# ==========================================================================================================================
# ==========================================================================================================================

# Creating and printing Array elements
import array as arr

# 1. Create empty then add
a = arr.array('i', [])  # empty
a.append(10)
a.append(20)
print(a)  # array('i', [10, 20])

# 2. Create directly with values
b = arr.array('i', [10, 20, 30, 40, 50])
print(b)

# 3. Create from user input
c = arr.array('i', [])
n = int(input("How many elements? "))
for i in range(n):
    val = int(input(f"Enter element {i}: "))
    c.append(val)
print("Your array:", c)

# Method 2: Using List (what you will actually use 99% time)
# 1. Direct creation
arr = [10, 20, 30, 40, 50]
print(arr)  # [10, 20, 30, 40, 50]

# 2. With loop
arr = []
for i in range(5):
    arr.append(i * 10)
print(arr)  # [0, 10, 20, 30, 40]

# 3. From user input
arr = []
n = int(input("How many elements? "))
for i in range(n):
    x = int(input("Enter number: "))
    arr.append(x)
print(arr)
