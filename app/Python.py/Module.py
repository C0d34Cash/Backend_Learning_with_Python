# A module is just a .py file containing functions/classes you can reuse.
# For Backend, this is how you organize code.
import math
from math import sqrt, ceil, pow, floor
num = 35 
result = math.sqrt(35)
result = math.pow(3,5)
print(result)
result1 = math.ceil(59.7)
result2 = math.floor(67.9)
print(result2)
print(result1)

# 2. Different Ways to Import
import math                 # full import
import math as m            # alias
from math import sqrt       # specific function
from math import *          # all (avoid this in backend)


# 3. Built-in Modules You MUST know for Backend
import os            # file paths, env variables
import sys           # system
import json          # API data
import datetime      # dates
import random        # tokens
import pathlib       # better file handling

print(os.getenv("PORT"))
print(datetime.datetime.now())

print("***********************************")

# PRACTICE PROBLEM
import math
x = 10.7
y = 3
print(math.ceil(x))
print(math.fabs(x))
print(pow(y,2))