name = input("What's your name? ")
print("Welcome",name,"to this adventure!")

print("You are in a dark forest.")
print("There's already two different paths you can continue your journey on.")
answer = input("Which one do you choose? Left or right? ").lower()
if answer == "left":
    print("You chose the path on the left side.")
    print("You see a river.")
    print("Do you swim across, or try to find a bridge?")
    answer = input("So swim across, or find a bridge? ").lower()
    if answer == "swim across":
        print("You swam across, and you were eaten by an aligator. You lost.")
    elif answer == "find a bridge":
        print("You walked miles, and didn't find anything. You lost.")
    else:
        print("Not a valid option. You lost.")
elif answer == "right":
    print("You chose the path on the right side.")
    print("You see a wolf.")
    print("Do you want to make friends with the wolf, or run away from it?")
    answer = input("So make friends, or run away? ").lower()
    if answer == "make friends":
        print("You give the wolf a little snack.")
        print("He likes it, so he won't hurt you.")
        print("You see an old man in the trees.")
        print("Do you try to talk to him or ignore him?")
        answer = input("So talk or ignore? ").lower()
        if answer == "talk":
            print("He helps you getting out of the forest. You win.")
        elif answer == "ignore":
            print("You ignore him, but you don't where the exit is. You lost.")
        else:
            print("Not a valid option. You lost.")
    elif answer == "run away":
        print("The wolf is way faster then you. You lost.")
    else:
        print("Not a valid option. You lost.")
else:
    print("Not a valid option. You lost.")

print("Thanks for playing,",name)