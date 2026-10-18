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