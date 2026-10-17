# for loop = runs for each item in a sequence.
# While loop needs i = 1, i <= 5, i += 1 all manual.
# For loop does it automatically.

# BASIC SYNTAX
for i in range(1, 6):
    print(i)
# 1 2 3 4 5

# A) Numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(i) # even

# B) String - letter by letter
for ch in "python":
    print(ch)

# C) List
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)


# NESTED FOR LOOP, SAME AS WHILE BUT CLEANER
# This while code:
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(j, end=" ")
        j += 1
    print()
    i += 1

# Same in for loop - 2 lines only:
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()