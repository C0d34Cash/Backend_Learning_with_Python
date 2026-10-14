# # Set - Unordered collection of unique items.
# # 3 main rules:
# # No duplicates - Every element must be unique
# # Unordered - No index my_set[0] -> ERROR, no order
# # Mutable - You can add/remove items, but elements themselves must be immutable

# set1 = {1, 2, 3, 4, 5} # set of integers
# print(set1) # printing the set

# 21 in set1 # checking if 21 is in the set
# print(21 in set1) # printing the result of the check

# len(set1) # finding the length of the set
# print(len(set1)) # printing the length of the set

# type(set1) # checking the type of the variable set1
# print(type(set1)) # printing the type of the variable set1

# set2 = {}
# print(type(set2)) # checking the type of the variable set2

# set3 = set("abcdmop")
# print(set3) # printing the set

# set4 = set("bcdanpx") # set of integers from a list

# # 1. UNION ( | or union() )
# # All elements from both sets. A ∪ B
# # A = {1, 2, 3, 4}
# # B = {3, 4, 5, 6}
# # print(A | B) # {1, 2, 3, 4, 5, 6}
# # print(A.union(B)) # same
# #Combines, removes duplicates. Like A + B.




# # 2. INTERSECTION ( & or intersection() )
# # Only common elements. A ∩ BpythonA = {1, 2, 3, 4}
# # B = {3, 4, 5, 6}
# # print(A & B) # {3, 4}
# # print(A.intersection(B)) # sameOnly what exists in BOTH.


# print("\n\n\n\n")
# print(set4 - set1) # difference of set4 and set1 (elements in set4 but not in set1)

# print(set4.difference(set1)) # same as above

# print(set4 ^ set1) # symmetric difference of set4 and set1 (elements in either set4 or set1 but not in both)

# print(set4.symmetric_difference(set1)) # same as above

# print(set4 & set1) # intersection of set4 and set1 (common elements in both sets)

# print(set4.intersection(set1)) # same as above

# print(set4 | set1) # union of set4 and set1 (all unique elements from both sets)

# print(set4.union(set1)) # same as above

# print(set4.isdisjoint(set1)) # checking if set4 and set1 have no common elements (returns True if they are disjoint, False otherwise)

# print(set4.issubset(set1)) # checking if set4 is a subset of set1 (returns True if all elements of set4 are in set1, False otherwise)

# print(set4.issuperset(set1)) # checking if set4 is a superset of set1 (returns True if all elements of set1 are in set4, False otherwise)

# print(set4.add(6)) # adding an element to set4
# print(set4) # printing set4 after adding an element

# print(set4.remove(6)) # removing an element from set4
# print(set4) # printing set4 after removing an element

# print(set4.discard(6)) # discarding an element from set4 (does not raise an error if the element is not present)
# print(set4) # printing set4 after discarding an element




#PRACTICE PROBLEM FROM TELUSKO
a = set("python")
b = set("telusko")
print(a & b) # intersection of sets a and b (common elements in both sets)