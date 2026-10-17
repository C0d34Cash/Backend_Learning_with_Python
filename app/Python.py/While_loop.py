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

