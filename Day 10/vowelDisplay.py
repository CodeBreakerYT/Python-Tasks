file = open("data.txt", "r")

for line in file:

    text = line.strip()

    if text != "" and text[0] in "AEIOUaeiou":
        print(text)

file.close()