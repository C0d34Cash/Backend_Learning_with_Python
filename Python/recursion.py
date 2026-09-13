# Function calls itself

def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

add_one(0)   # Prints till 9 

print("\n\n\n\n")

def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)      # Prints till 10