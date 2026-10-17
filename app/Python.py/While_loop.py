
# while loop = keeps running WHILE the condition is True.

# STRUCTURE
# initialization
# while condition:
    # pass
    # body
   #  update

# LOOP COUNTER
# Loop Counter = a variable that COUNTS how many times the loop has run.
# It's just a normal variable, usually named i, count, n.
# i = 1  # <-- this is the LOOP COUNTER

i = 1 # <-- This is the initialization
while i <= 5:
    print(f"Round {i}")
    i = i + 1  # <-- we update the counter

# 3 JOBS OF A LOOP COUNTER
# 1.Start - i = 1
# 2.Check - while i <= 5:
# 3.Update - i = i + 1 (otherwise infinite loop)

# BAD - INFINITE LOOP
# while True:
#     print("hello") # will print forever

# GOOD - WITH COUNTER
count = 0
while count < 3:
    print("hello")
    count += 1 # counter stops it after 3 times

# SO IN SHORT, LOOP COUNTER = i THAT YOU INCREASE/DECREASE TO CONTROL THE LOOP.



# Nested while = one while inside another
#  whileOuter loop = Rows
# Inner loop = Columns

# BASIC STRUCTURE
# outer
i = 1
while i <= 3:
    
    # inner
    j = 1
    while j <= 3:
        print(j, end=" ")
        j += 1
    print() # new line
    i += 1

# TABLE OF 1 TO 3
    i = 1
while i <= 3:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print("---")
    i += 1

# STAR PATTERN
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# MATRIX /ROWS x COLS
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
# (1,1) (1,2)
# (2,1) (2,2)


# GOLDEN-RULE
# Always RE-initialize inner counter j = 1 inside outer loop. 
# If you put it outside, inner loop will run only once.