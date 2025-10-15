word = input("Enter a word: ").lower()

vowels = "aeiou"

dictionary = {}.fromkeys(vowels,0)

for i in word:
    if i in vowels:
        dictionary[i] += 1

for i in dictionary:
    print(i,"-->",dictionary[i])
