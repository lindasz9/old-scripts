principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principle can't be less then or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Ineterest rate can't be less then or equal to zero")

while time <= 0:
    time = int(input("Enter the years: "))
    if time <= 0:
        print("Time can't be less then or equal to zero")

total = principal * pow((1 + rate / 100),time)

if time == 1:
    print("Balance after",time,"year: $",total)
else:
    print("Balance after",time,"years: $",total)