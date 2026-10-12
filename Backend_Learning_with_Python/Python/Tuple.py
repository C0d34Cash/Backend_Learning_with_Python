Tuple = (1, 2, 3, 4, 5)
print(type(Tuple)) # checking the type of the variable Tuple
min(Tuple) # finding the minimum element in the tuple
print(min(Tuple)) # printing the minimum element in the tuple
max(Tuple) # finding the maximum element in the tuple
print(max(Tuple)) # printing the maximum element in the tuple
Tuple[2] # indexing the third element in the tuple
print(Tuple[2]) # printing the third element in the tuple


# Tuple[2] = 6 # trying to change the value of the third element in the tuple (this will raise an error because tuples are immutable)

len(Tuple) # finding the length of the tuple
print(len(Tuple)) # printing the length of the tuple

TupleAnother = (6, 7, 8, 9, 10)
print(TupleAnother) # printing the second tuple
num, name, pi, boolean, string = TupleAnother # unpacking the tuple into variables
print(num) # printing the unpacked variables

TupleMixed = (1, 'Debojyoti', [4,8,9], True) # tuple of mixed data types
print(TupleMixed) # printing the mixed-type tuple

# TupleMixed[2] = 6.28 # trying to change the value of the third element in the mixed-type tuple (this will raise an error because tuples are immutable)

TupleMixed [2][1] = 7 
print(TupleMixed) # printing the mixed-type tuple after changing the value of the third element

print(5 in TupleAnother) # checking if 5 is in the second tuple

print("debojyoti" in TupleMixed) # checking if "debojyoti" is in the mixed-type tuple


# PRACTICE EXCERCISE
TUPLE = (1, 2, 3, 4, 5)
x = TUPLE[2]
y = TUPLE[4]
print(x + y) # adding the third and fifth elements of the tuple and printing the result