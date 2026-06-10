file = open("data.txt", "r")

data = file.read().lower()

word = input("Enter word: ").lower()

count = data.split().count(word)

print("Frequency =", count)

file.close()