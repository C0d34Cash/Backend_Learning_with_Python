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

mynewtotal = add_one(0) # add_one returns 10 at the end
print(mynewtotal)       # so you print that 10