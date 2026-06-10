file = open("student.txt", "r")

while True:
    line = file.readline()

    if line == "":
        break

    print(line)

file.close()