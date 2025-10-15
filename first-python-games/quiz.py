import time

def new_game():
    time.sleep(0.5)
    guesses = []
    correct_guesses = 0
    question_num = 0
    for key in questions:
        if not(question_num == 0):
            print("---------------------------------")
        time.sleep(0.5)
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter: A,B,C, or D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        time.sleep(0.5)
    display_score(correct_guesses, guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses):
    time.sleep(0.5)
    print("---------------------------------")
    print("RESULTS:")
    print("---------------------------------")
    time.sleep(0.5)
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    time.sleep(0.5)
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    time.sleep(0.5)
    print("Your score is "+str(score)+"%")

def play_again():
    time.sleep(1)
    response = input("Wanna play again? Yes or no? ").lower()
    if response == "yes":
        return True
    else:
        return False

questions = {
    "What sport do I play?":"D",
    "What's my favourite pet?":"A",
    "What month was I born?":"B",
    "What city do I want to travel to?":"D"}
options = [["A: volleyball","B: football","C: tennis","D: handball"],
           ["A: cat","B: dog","C: hamster","D: rabbit"],
           ["A: february","B: may","C: july","D: november"],
           ["A: New York","B: Barcelona","C: London","D: Paris"]]

new_game()

while play_again():
    new_game()

time.sleep(0.5)
print()
print("Thanks for playing!")