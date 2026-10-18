import array as ar
m = ar.array("f", [2.5,4.8,-3.2,6.7])
m.reverse()
for element in m:
    print(element)

# 1. List as Array (Most Common)
arr = [10, 20, 30]

arr.append(40)      # [10,20,30,40]
arr.insert(1, 15)   # [10,15,20,30,40]
arr.extend([50,60]) # [10,15,20,30,40,50,60]
arr.pop()           # remove last -> [10,15,20,30,40,50]
arr.pop(0)          # remove index 0
arr.remove(20)      # remove value 20
arr.sort()          # sort ascending
arr.reverse()       # reverse
arr.index(30)       # find index of 30
arr.count(20)       # how many 20s
len(arr)            # length
sum(arr)            # sum
max(arr) / min(arr) # max/min
arr.clear()         # delete all

# 2. array Module (Real Array)
import array as arr
a = arr.array('i', [10, 20, 30])

# Same as list + these extra:
a.typecode          # 'i'
a.itemsize          # size in bytes
a.buffer_info()     # (memory_address, length)
a.tobytes()         # to bytes
a.tolist()          # to list
a.fromlist([40,50]) # add from list



import array as arr
arr1 = arr.array("i",[77,8,9,43])
arr2 = arr.array(arr1.typecode,arr1.tolist())
arr1[2]= 87
print(arr1)
print(arr2)


import array as arr
arr1 = arr.array("i",[77,8,9,43])
arr2 = arr.array(arr1.typecode,(n for n in arr1))
arr1[2]= 87
print(arr1)
print(arr2)


from array import *
arr = array("i",[10,20,30])
arr.append(40)
arr.reverse()
print(arr[0])

# 3. NumPy Array (For Data Science - Most Powerful). This is what companies actually use:
import numpy as np
a = np.array([10, 20, 30, 40])

# Creation
np.zeros(5)              # [0,0,0,0,0]
np.ones(5)               # [1,1,1,1,1]
np.arange(0, 10, 2)      # [0,2,4,6,8]
np.linspace(0, 10, 5)    # 5 numbers between 0-10

# Math functions - IMPOSSIBLE in list/array module
a + 10                   # [20,30,40,50] - add 10 to all
a * 2                    # [20,40,60,80]
np.sum(a)                # 100
np.mean(a)               # average
np.max(a) / np.min(a)
np.sort(a)
np.sqrt(a)               # square root of each
np.reshape(a, (2,2))     # convert to 2D

# Important for exams
a.shape                  # (4,) - size
a.size                   # 4 - total elements
a.dtype                  # int64