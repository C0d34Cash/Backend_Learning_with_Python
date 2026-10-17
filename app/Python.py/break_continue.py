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