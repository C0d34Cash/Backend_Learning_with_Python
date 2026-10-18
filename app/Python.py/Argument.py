# TYPE OF ARGUMENTS

# Default Arguments in Python
# Default argument = value that is used if you don't pass anything.
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()          # Hello, Guest -> uses default
greet("Rahul")   # Hello, Rahul -> uses your value

# IMPORTANT RULES
# Rule 1: Default must be at the end
# CORRECT
def func(a, b=10):
    print(a, b)

# WRONG - will give error
# def func(a=10, b): # Here is the error
    print(a, b)

# Rule 2: You can have many defaults
def student(name="Unknown", age=18, city="Kolkata"):
    print(f"{name}, {age}, {city}")

student()  # Unknown, 18, Kolkata
student("Rahul")  # Rahul, 18, Kolkata
student("Rahul", 21)  # Rahul, 21, Kolkata
student("Rahul", 21, "Delhi")  # Rahul, 21, Delhi
student(age=25)  # Unknown, 25, Kolkata - using keyword

# Rule 3: Default is evaluated only ONCE - BIG TRAP (Interview Question)
# WRONG WAY - Never use list as default
def add_item(item, my_list=[]):
    my_list.append(item)
    print(my_list)

add_item(10)  # [10]
add_item(20)  # [10, 20] - WTF! It remembered old list!

# CORRECT WAY
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    print(my_list)

add_item(10)  # [10]
add_item(20)  # [20] - Correct!

# Example with Array
import array as arr

def create_array(values, typecode='i'):  # 'i' is default
    a = arr.array(typecode, values)
    return a

# Uses default 'i'
a1 = create_array([10, 20, 30])
print(a1)  # array('i', [10, 20, 30])

# Override default with 'd' for float
a2 = create_array([2.5, 4.8, -3.2], typecode='d')
print(a2)  # array('d', [2.5, 4.8, -3.2])

# Your Float Array Question with Default Argument
import array as arr

def print_positive(arr_data, skip_negative=True):  # skip_negative is default
    for x in arr_data:
        if skip_negative and x < 0:
            continue
        print(x)

my_arr = arr.array('d', [2.5, 4.8, -3.2, 6.7])

print_positive(my_arr)  # Uses default True -> skips -3.2
print("---")
print_positive(my_arr, False)  # Override -> prints -3.2 also
# In one line: Default argument = backup value.

print("========================================================================")
print("========================================================================")


# HANDLING UNEXPECTED ARGUMENTS
# When someone passes wrong number of arguments, Python throws error. 
# We handle it with _args, _*kwargs and error handling.
def add(a, b):
    print(a + b)

# add(10, 20, 30)  # ERROR! add() takes 2 but 3 given

# Solution 1: *args for extra positional arguments
def add(a, b, *extra):
    print(f"a={a}, b={b}")
    print(f"Extra unwanted: {extra}")
    print(a + b)

add(10, 20, 30, 40, 50)
# a=10, b=20
# Extra unwanted: (30, 40, 50)
# 30
#  Solution 2: **kwargs for extra keyword arguments
def student(name, age):
    print(f"{name}, {age}")

def safe_student(name, age, **extra):
    print(f"{name}, {age}")
    if extra:
        print(f"Ignoring extra info: {extra}")

safe_student(name="Rahul", age=21, city="Kolkata", hobby="Coding")
# Rahul, 21
# Ignoring extra info: {'city': 'Kolkata', 'hobby': 'Coding'}

#  Solution 3: Handle EVERYTHING (Best for real projects)
def super_safe(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

super_safe(10, 20, 30, name="Rahul", age=21)
# Positional: (10, 20, 30)
# Keyword: {'name': 'Rahul', 'age': 21}

# Solution 4: Try-Except (For wrong types)
def add(a, b):
    try:
        print(a + b)
    except TypeError:
        print("Error: Please pass only numbers!")
    except Exception as e:
        print(f"Unexpected error: {e}")

add(10, 20)      # 30
add(10, "Rahul") # Error: Please pass only numbers!

# Full Example - Your Array Case
import array as arr

def create_float_array(*values, **options):
    # options can have typecode='d' or 'f'
    typecode = options.get('typecode', 'd')  # default 'd'
    
    # Filter only numbers, ignore unexpected strings etc
    clean_values = []
    for v in values:
        if isinstance(v, (int, float)):
            clean_values.append(v)
        else:
            print(f"Skipping invalid value: {v}")

    if 'extra' in options:
        print(f"Note: extra option ignored: {options['extra']}")

    return arr.array(typecode, clean_values)

# Test - passing unexpected arguments
my_arr = create_float_array(2.5, 4.8, "hello", -3.2, 6.7, typecode='d', extra="test")
print(my_arr)

for x in my_arr:
    if x < 0:
        continue
    print(x)


print("================================================================================")
print("================================================================================")

# Variable Length Arguments - _args and __kwargsThis lets you pass ANY number of arguments.
# 1. _args - Many Values (Tuple)* means pack into tuple.
def total(*numbers):
    print(numbers)  # tuple
    print(type(numbers))
    s = 0
    for n in numbers:
        s += n
    print(f"Sum = {s}")

total(10, 20)              # (10, 20) Sum = 30
total(10, 20, 30, 40)      # (10, 20, 30, 40) Sum = 100
total()                    # () Sum = 0
# 2. *_kwargs - Many Key-Value Pairs (Dictionary)_* means pack into dictionary.
def details(**info):
    print(info)  # dict
    for key, value in info.items():
        print(f"{key} : {value}")

details(name="Rahul", age=21)
# {'name': 'Rahul', 'age': 21}
# name : Rahul
# age : 21

details(name="Rahul", age=21, city="Kolkata", marks=90)
# 3. Both Together - The Order Matters!
def all_in_one(a, *args, **kwargs):
    print(f"a = {a}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

all_in_one(10, 20, 30, 40, name="Rahul", city="Kolkata")
# a = 10
# args = (20, 30, 40)
# kwargs = {'name': 'Rahul', 'city': 'Kolkata'}

print("******ORDER: normal -> _args -> *kwargs******")

# 4. Real Examples for You
# Example 1: Your Float Array Problem with Variable Args
import array as arr

def make_array_and_print(*values):
    # values can be any length
    my_arr = arr.array('d', values)
    
    for x in my_arr:
        if x < 0:
            continue
        print(x)

make_array_and_print(2.5, 4.8, -3.2, 6.7)
# 2.5
# 4.8
# 6.7

make_array_and_print(1.1, -2.2, 3.3, -4.4, 5.5, 100.5)
# 1.1
# 3.3
# 5.5
# 100.5
# Example 2: Average Function
def average(*marks):
    if len(marks) == 0:
        print("No marks given")
        return
    avg = sum(marks) / len(marks)
    print(f"Average = {avg}")

average(80, 90, 70)  # Average = 80.0
average(100, 95, 98, 92, 96)  # Average = 96.2
#Example 3: Student Report
def report(name, *marks, **details):
    print(f"Name: {name}")
    print(f"Marks: {marks} -> Total: {sum(marks)}")
    print(f"Other details: {details}")

report("Rahul", 80, 90, 85, age=21, city="Kolkata", branch="CSE")
# 5. Unpacking with _ and _* (Reverse)
def add(a, b, c):
    print(a + b + c)

nums = [10, 20, 30]
add(*nums)  # Same as add(10,20,30)

data = {'a':10, 'b':20, 'c':30}
add(**data)  # Same as add(a=10, b=20, c=30)
# ONE LINE TO REMEMBER
#_args for values, _*kwargs for names = values.

print("========================================")
print("========================================")

# KEYWORD ARGUMENTS
# Rules to Remember
#. Positional first, keyword second
#. Keyword order doesn't matter
#. Once you use keyword, all after must be keyword
#. **kwargs collects all extra keywords as dict

# Keyword argument = you tell the function name = value1.
#  BasiC:
def student(name, age, city):
    print(f"{name} {age} {city}")

# Positional - order must be correct
student("Rahul", 21, "Kolkata")  # Rahul 21 Kolkata

# Keyword - order doesn't matter
student(age=21, city="Kolkata", name="Rahul")  # Same output
student(city="Kolkata", name="Rahul", age=21)  # Same output

# Mixed - positional first, then keyword
student("Rahul", age=21, city="Kolkata")  # OK

# student(age=21, "Rahul", "Kolkata")  # ERROR! positional after keyword not allowed

# 2. With Default Arguments (Main Use)
def create_profile(name, age=18, city="Kolkata", branch="CSE"):
    print(f"{name} | {age} | {city} | {branch}")

create_profile("Rahul")  
# Rahul | 18 | Kolkata | CSE - all defaults

create_profile("Rahul", age=21)  
# Rahul | 21 | Kolkata | CSE - change only age

create_profile("Rahul", city="Delhi", age=22)  
# Rahul | 22 | Delhi | CSE - skip age order, use keyword

create_profile(branch="ECE", name="Anu", city="Mumbai")  
# Anu | 18 | Mumbai | ECE - any order possible

# 3. **kwargs = Many Keyword Arguments
def details(**kwargs):
    print(kwargs)

details(name="Rahul", age=21)  
# {'name': 'Rahul', 'age': 21}

details(name="Rahul", age=21, city="Kolkata", marks=90)  
# {'name': 'Rahul', 'age': 21, 'city': 'Kolkata', 'marks': 90}

# 4. Forcing Keyword Only (Advanced - Interview)
# Everything after * must be keyword
def func(a, b, *, c, d):
    print(a, b, c, d)

func(10, 20, c=30, d=40)  # OK
# func(10, 20, 30, 40)    # ERROR! c,d must be keyword

# Practical use - prevent mistakes
def create_array(*values, typecode='d'):
    import array as arr
    return arr.array(typecode, values)

# typecode MUST be keyword, can't mess order
arr1 = create_array(2.5, 4.8, -3.2, typecode='f')

# 5. Your Array Example with Keywords
import array as arr

def print_array(data, skip_negative=True, reverse=False):
    if reverse:
        data = arr.array(data.typecode, reversed(data))
    
    for x in data:
        if skip_negative and x < 0:
            continue
        print(x, end=" ")

my_arr = arr.array('d', [2.5, 4.8, -3.2, 6.7])

print_array(my_arr)  # 2.5 4.8 6.7 - uses defaults

print_array(my_arr, skip_negative=False)  
# 2.5 4.8 -3.2 6.7 - keyword changes behavior

print_array(my_arr, reverse=True, skip_negative=False)  
# 6.7 -3.2 4.8 2.5 - order doesn't matter because keywords

print_array(data=my_arr, reverse=True)  
# 6.7 4.8 2.5 - even data as keyword

# ONE LINE : KEYWORD ARGS = FREEDOM FROM ORDER.

print("========================================")
print("=========================================")

# Definition
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>

func(name="Rahul", age=21)
# {'name': 'Rahul', 'age': 21}

func(name="Rahul", age=21, city="Kolkata", branch="CSE")
# {'name': 'Rahul', 'age': 21, 'city': 'Kolkata', 'branch': 'CSE'}
# *kwargs always gives you a DICTIONARY_.

# 2. Why We Need It?
# Without _*kwargs you must fix number of keywords:
# BAD - Only 2 allowed
def student(name, city):
    print(name, city)

#  student"Rahul", city="Kolkata", age=21)  # ERROR

# GOOD - Any number allowed 
def student(**kwargs):
    print(kwargs)

student(name="Rahul", city="Kolkata", age=21, marks=90)  # Works

# 3. Looping Through kwargs
def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show(name="Rahul", age=21, city="Kolkata")
# name = Rahul
# age = 21
# city = Kolkata

# 4. Mixing with Everything - FINAL FORM
def final(a, b=10, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")     # tuple
    print(f"kwargs = {kwargs}") # dict
    print("-----")

final(1, 2, 3, 4, 5, name="Rahul", age=21)
# a = 1
# b = 2
# args = (3, 4, 5)
# kwargs = {'name': 'Rahul', 'age': 21}



# PRACTICE PRBLEM
 # def greet (name, msg= "welcome to Telusko") # it's wrong because there is no ":"
def greet (name, msg= "welcome to Telusko"): # Now it's right
    print("Hello",name,msg)
greet("Navin")
greet("Harsh","Good to see you again")