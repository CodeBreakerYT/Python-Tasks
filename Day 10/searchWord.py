file = open("student.txt", "r")

data = file.read()

word = input("Enter word to search: ")

if word in data:
    print("Found")
else:
    print("Not Found")

file.close()