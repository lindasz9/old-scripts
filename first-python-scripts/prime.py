number = input("Enter a number: ")
oszto = 2
hanyados = int(number) / oszto
number_2 = number

while not(hanyados == 1):
    hanyados = int(number) / oszto
    if oszto == int(number_2):
        print("This number is prime")
        break
    if hanyados == int(hanyados):
        if not(hanyados == 0):
            print(str(int(number)) + "|" + str(oszto))
            number = int(number) / oszto
    else:
        oszto += 1

if not(oszto == int(number_2)):
    print(1)

