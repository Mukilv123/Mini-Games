import random

# prompts the user to make a move
user = input("Please pick rock, paper, or scissors: ")
opponent = random.choice(["rock", "paper", "scissors"])

# Compares users choice vs. computers
while True:
    if (user == opponent):
        print("It was a tie")
    elif (user=="rock" and opponent=="scissors") or (user=="scissors" and opponent=="paper") or (user=="paper" and opponent=="rock"):
        print("You win")
    else:
        print("You lost")

    rematch = input("Please hit p to play again or q to quit: ")
    if (rematch == "q"):
        break

    user = input("Please pick rock, paper, or scissors: ")
    opponent = random.choice(["rock", "paper", "scissors"])