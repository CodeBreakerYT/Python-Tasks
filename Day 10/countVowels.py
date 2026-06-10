file = open("student.txt", "r")

data = file.read()

count = 0

for ch in data:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels =", count)

file.close()