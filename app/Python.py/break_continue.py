# break = Stop the loop fully and exit
for i in range(1, 11):
    if i == 5:
        break  # stop at 5
    print(i)

# Output: 1 2 3 4

# Find first even
for i in range(1, 10):
    if i % 2 == 0:
        print(f"Found {i}")
        break

# continue = Skip this one round, go to next
for i in range(1, 11):
    if i == 5:
        continue  # skip 5
    print(i)

# Output: 1 2 3 4 6 7 8 9 10 (5 missing)
# Use: When you want to ignore some values.
# Print only even, skip odd
for i in range(1, 11):
    if i % 2 != 0:
        continue  # skip odd
    print(i) # 2 4 6 8 10

# Side by Side Comparison
numbers = [1, 2, 3, 4, 5, 6]

# break
for n in numbers:
    if n == 4:
        break
    print(n)  # 1 2 3 -> stops at 4

print("---")

# continue
for n in numbers:
    if n == 4:
        continue
    print(n)  # 1 2 3 5 6 -> only 4 skipped

# In while loop - same
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue # careful: must update before continue, else infinite loop
    if i == 8:
        break
    print(i)
    i += 1
# 1 2 3 4 6 7