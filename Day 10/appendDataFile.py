file = open("student.txt", "a")

for i in range(3):
    name = input("Enter new record: ")
    file.write(name + "\n")

file.close()

print("Records Added")