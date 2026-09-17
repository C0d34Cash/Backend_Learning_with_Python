# Primitive ways of functioning strings
person = "Dave"
coins = 3
print ("\n" + person + " has " + str(coins) + "coins left.") 

message = "\n%s has %s coins left." % (person,coins)
print(message)

message = "\n{} has {} coins left.".format(person,coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins,person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    person= person,coins=coins
    )
print(message)

player ={ "person" : "Dave" , "coins" : 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

print("\n\n\n\n")

###################
# f-strings! That's the way!
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {4*5} coins left."
print(message)

message = f'\n{player["person"]} has {5*10} coins left.'
print(message)