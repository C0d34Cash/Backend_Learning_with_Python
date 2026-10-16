# # elif = else + if. Means "otherwise, check this".
# # Use it when you have more than 2 options.

# # WITHOUT ELIF
# marks = int(input("Enter your marks arsehole: "))
# if marks >= 90:
#     print("A")
# else:
#     if marks >= 60:
#         print("B")
#     else:
#         if marks >= 33:
#             print("C")
#         else:
#             print("Fail")

# # WITH ELIF
# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 33:
#     print("Grade C")
# else:
#     print("Fail")


# PRACTICE PROBLEM
score = int(input("Enter the batsman's score: "))
if score >= 90:
    print("Grade A+")
elif score >= 75:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")