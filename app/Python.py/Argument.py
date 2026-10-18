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