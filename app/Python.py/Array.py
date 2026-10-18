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

