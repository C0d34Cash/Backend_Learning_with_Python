# TYPE OF ARGUMENTS
# 1. Positional Argument - order matters
def add(a, b):
    print(a + b)

add(10, 20)  # a=10, b=20

# 2. Keyword Argument - name matters, order doesn't
add(b=20, a=10)  # same result

# 3. Default Argument - if you don't give, it uses default
def greet(name="Guest"):
    print(f"Hello {name}")

greet()         # Hello Guest
greet("Rahul")  # Hello Rahul

# 4. Variable Length *args - takes many values as tuple
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(total)

sum_all(1, 2, 3)        # 6
sum_all(10, 20, 30, 40) # 100

# 5. Variable Length **kwargs - takes many as dictionary
def show_info(**info):
    for key, value in info.items():
        print(f"{key} = {value}")

show_info(name="Rahul", age=21, city="Kolkata")
# name = Rahul
# age = 21
# city = Kolkata