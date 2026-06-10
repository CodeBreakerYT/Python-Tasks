file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Words =", len(words))

file.close()