file = open("marks.txt", "w")

for i in range(3):
    name = input("Name: ")
    marks = int(input("Marks: "))

    file.write(name + "," + str(marks) + "\n")

file.close()

file = open("marks.txt", "r")

print("Students with marks greater than 75:")
for line in file:
    name, marks = line.strip().split(",")

    if int(marks) > 75:
        print(name)

file.close()