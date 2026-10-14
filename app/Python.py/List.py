# List is an ordered, mutable collection of items in Python,
#  written with [].
# In one line:List = Shopping bag, you can add, 
# remove, change items anytime.

nums = [1, 2, 3, 4, 5] # list of integers
# print(nums) # printing the listS
# print(nums[0]) # indexing starts from 0
# print(nums[-1]) # indexing from the end
# print(nums[0:3]) # slicing from index 0 to 2
# print(nums[0:]) # slicing from index 0 to end
# print(nums[:3]) # slicing from start to index 2

names = ['Debojyoti', 'John', 'Alice', 'Bob'] # list of strings
# print(names) # printing the list
# print(names[0]) # indexing starts from 0
# print(names[-1]) # indexing from the end
# print(names[0:3]) # slicing from index 0 to 2
# print(names[0:]) # slicing from index 0 to end
# print(names[:3]) # slicing from start to index 2

Mixed = [1, 'Debojyoti', 3.14, True] # list of mixed data types
# print(Mixed) # printing the list

# Mix = [nums, nums, Mixed] # list of lists
# print(len(Mix)) # length of the list of lists
# print(Mix) # printing the list of lists
# print(Mix[0]) # indexing the first list
# print(Mix[0][0]) # indexing the first element of the first list
# print(Mix[2][3]) # indexing the fourth element of the third list

print(" ")

# nums.append(6) # adding an element to the end of the list
# print(nums) # printing the list after adding an element

# nums.pop(3) # removing the element at index 3 from the list
# print(nums) # printing the list after removing the element at index 3

# nums.count(2) # counting the number of occurrences of 2 in the list
# print(nums) # printing the list after counting the occurrences of 2

# nums.sort() # sorting the list in ascending order
# print(nums) # printing the list after sorting

# print(nums.reverse()) # reversing the list

# (nums.insert(2,4)) # inserting 4 at index 2 in the list
# print(nums)

# print(nums.index(4)) # finding the index of the first occurrence of 4 in the list

# # (nums.remove(4)) # removing the first occurrence of 4 from the list
# # print(nums)

# del nums[2:5] # deleting the elements from index 2 to 4 from the list
# print(nums) # printing the list after deleting the elements from index 2 to 4

# nums.extend([6, 7, 8]) # extending the list by adding elements from another list
# print(nums) # printing the list after extending it with another list

# nums[2:5] = [9, 10, 11] # replacing the elements from index 2 to 4 with new elements
# print(nums) # printing the list after replacing the elements from index 2 to 4 with new elements

# min(nums) # finding the minimum element in the list
# print(min(nums)) # printing the minimum element in the list

# max(nums) # finding the maximum element in the list
# print(max(nums)) # printing the maximum element in the list

# sum(nums) # finding the sum of all elements in the list
# print(sum(nums)) # printing the sum of all elements in the list


a =   [1, 2, 3, 4, 5]
b =   [6, 7, 8, 9, 10]
print((a[:2]+ b[1:])[-3]) # concatenating the first two elements of list a with the last three elements of list b and then printing the third element from the end of the resulting list