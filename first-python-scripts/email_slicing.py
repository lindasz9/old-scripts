email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print("Your username is",username,"and domain is",domain)