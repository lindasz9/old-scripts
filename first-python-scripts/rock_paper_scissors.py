import random
import time

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)

    player = input("Rock, paper or scissors? ").lower()

    while player not in choices:
        player = input("I said: rock, paper or scissors? ").lower()

    print("player: "+player)
    time.sleep(1)
    print("computer: "+computer)
    time.sleep(1)

    if player == computer:
        print("TIE")
    elif player == "rock":
        if computer == "paper":
            print("LOSE")
        if computer == "scissors":
            print("WIN")
    elif player == "paper":
        if computer == "rock":
            print("WIN")
        if computer == "scissors":
            print("LOSE")
    elif player == "scissors":
        if computer == "rock":
            print("LOSE")
        if computer == "paper":
            print("WIN")

    time.sleep(1)

    again = input("Wanna play again? Yes or no? ").lower()
    if again != "yes":
        break
print("Thanks for playing!")




