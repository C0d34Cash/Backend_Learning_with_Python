import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    playerchoice = input(
        "\nEnter .... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice) # <-- This line was not indented

    if player < 1 or player > 3:
        sys.exit("Invalid choice. Please enter a number between 1 and 3.")
        
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print(f"\nYou chose " + str(RPS(player)).replace("RPS."," ") + ".")
    print(f"Computer chose " + str(RPS(computer)).replace("RPS."," ") +".\n")

    if player == 1 and computer == 3:
        print("🎉 you win!")
    elif player == 2 and computer == 1:
        print("🎉 you win!")
    elif player == 3 and computer == 2:
        print("🎉 you win!")
    elif player == computer:
        print("😒 It's a tie!")
    else:
        print("🐍 Python wins!")

    playagain = input("\n Play again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n  🎉🎉🎉🎉🎉 ")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye!")