import random

top = input("What should be the top number? ")

if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Please type a number larger then 0")
        quit()
else:
    print("Please type a number")
    quit()

random = random.randrange(1,top)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number")
        continue
    if guess == random:
        print("You got it!")
        break
    elif guess > random:
        print("Too large")
    else:
        print("Too low")

print("You got it in",guesses,"guesses")


