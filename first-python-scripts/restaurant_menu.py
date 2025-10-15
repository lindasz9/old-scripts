menu = {"pizza":3.00,
        "hamburger":4.00,
        "hotdog":3.50}
cart = []
total = 0

print("---------- MENU ----------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------- TOTAL -----------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: ${total:.2f}")
