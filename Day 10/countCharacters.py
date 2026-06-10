file = open("student.txt", "r")

data = file.read()

print("Characters =", len(data))

file.close()