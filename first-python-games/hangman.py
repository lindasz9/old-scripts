word = input("word: ")
letters = []
for a in word:
    letters.append(["_", a])
hearts = 5
guesses = []

while True:
    print()
    print("hearts:",hearts)
    for b in letters:
        print(b[0],end=" ")
    print()
    while True:
        guess = ""
        while len(guess.strip()) == 0:
            guess = input("guess: ").strip()
        print(guess)
        if guess in guesses:
            print("You've already guessed that")
        else:
            break
    guesses.append(guess)
    fails = 0
    for c in letters:
        if guess == c[1]:
            c[0] = guess
            c[1] = "_"
        else:
            fails += 1
    if fails == len(word):
        hearts -= 1
        print()
        print("-1 heart")
    end = True
    for d in letters:
        if d[0] == "_":
            end = False
    if end == True:
        print()
        print(word)
        print("WIN")
        break
    if hearts == 0:
        print()
        print("LOSE")
        print("the word was:",word)
        break