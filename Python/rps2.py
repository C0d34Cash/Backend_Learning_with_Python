import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



print(' ')
playerchoice = input("Enter .... \n1  for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
   sys.exit("Invalid choice. Please enter a number between 1 and 3.")
    
computerchoice = random.choice("123")

computer = int(computerchoice)

print(" ")
print(f"You chose " +  str(RPS(player)).replace("RPS."," ") + ".")
print(f"Computer chose " + str(RPS(computer)).replace("RPS."," ") +".")

if player == 1 and computer == 3:
   print("you win")
elif player == 2 and computer == 1:
   print("you win")
elif player == 3 and computer == 2:
   print("you win")
elif player == computer:
   print("It's a tie")
else:
   print("Computer wins")
