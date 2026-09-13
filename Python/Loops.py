value = 1
while value <=10:
    value += 1
    if value == 5:
        continue
    print(value)
else: 
    print("Value is now equal to " + str(value))

names = ["Debojyoti", "Sandipan","Ankan" ]
for x in names:
    print(x)


for x in names:
    if x == "Ankan":
        break
    print(x)

for x in range(4):
    print(x)

for x in range(2,4):
    print(x)


print("\n\n")
names = ["Debojyoti", "Sandipan","Ankan" ]
actions = ["reads","eats","codes"]

for name in names:
    for action in actions:
        print(name+ " " + action+ ".")

print("\n\n\n")
for action in actions:
    for name in names:
          print(name+ " " + action+ ".")