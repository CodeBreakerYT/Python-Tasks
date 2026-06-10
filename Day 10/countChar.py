file = open("data.txt", "r")

data = file.read()

digits = 0
alphabets = 0
special = 0

for ch in data:

    if ch.isdigit():
        digits += 1

    elif ch.isalpha():
        alphabets += 1

    else:
        special += 1

print("Digits =", digits)
print("Alphabets =", alphabets)
print("Special Characters =", special)

file.close()