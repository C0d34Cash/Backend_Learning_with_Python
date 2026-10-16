# # match case is like switch in other languages. 
# # Came in Python 3.10.It's a cleaner replacement for many if-elif-else.

# # SYNTAX:
# score = int(input("Enter score: "))

# match score:
#     case 90:
#         print("Exactly 90")
#     case 80:
#         print("Exactly 80")
#     case _:
#         print("Other score")  # _ means default / else

# # Grade example with match case example:
# score = int(input("Enter score: "))

# match score:
#     case s if s >= 90:
#         print("Grade A+")
#     case s if s >= 75:
#         print("Grade A")
#     case s if s >= 60:
#         print("Grade B")
#     case _:
#         print("Grade C")

# # Simple Day example (best use case)::
# day = int(input("Enter day number 1-7: "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")


# When to use what?
# if-elif-else -> for ranges (like >= 90, < 60)
# match case -> for exact values (like 1, 2, "Monday", "red")



# PRACTICE PROBLEM
num = int(input("Do you thing bustard: "))
match num % 3:
    case 0:
        print("Divisible by 3")
    case 1:
        print(" Remainder 1 when divided by 3")
    case _:
        print("Remainder 2 when divided by 3")