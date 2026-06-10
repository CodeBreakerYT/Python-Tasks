file = open("data.txt", "r")

data = file.read()

new_data = data.replace("Python", "Programming")

file.close()

file = open("data.txt", "w")

file.write(new_data)

file.close()

print("Replacement Done")