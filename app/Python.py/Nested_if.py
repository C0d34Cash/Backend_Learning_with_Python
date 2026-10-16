# Nested if = an if statement INSIDE another if statement.
# You check a second condition only if the first one is already true.

age = int(input("Enter your age bitch: "))
has_id = True

if age >= 18:
    print("You are adult")
    if has_id == True:
        print("You can Vote!")
    else:
        print("Get your ID first")
else:
    print("You are too young")


marks = int(input("enter what you got bustard: "))
if marks >= 50:
    print("Pass")
    if marks >= 75:
        print("Distintion")
    else:
        print("Average")
else:
    print("Fail")
print("End of evaluation")