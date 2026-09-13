# Function calls itself

def add_one(num):
    if (num >= 9):      # if num is 9 or more, STOP and return
        return num + 1  # return 10, but DON'T print it
    total = num + 1     # 1,2,3...
    print(total)        # prints here
    return add_one(total) # call again

add_one(0) # Prints till 9

print("\n\n\n\n")

def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

# Here i'm replacing recursion with loop

mynewtotal = add_one(0) # add_one returns 10 at the end
print(mynewtotal)       # so you print that 10

# METHOD 1: for loop - Best
for num in range(1, 11):
    print(num)

# METHOD 2: while loop - same logic as your recursion
num = 0
while num < 9:
    num = num + 1
    print(num)

mynewtotal = num + 1 # this is your last return 10
print(mynewtotal)