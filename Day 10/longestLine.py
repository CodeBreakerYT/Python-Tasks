file = open("student.txt", "r")

lines = file.readlines()

longest = max(lines, key=len)

print("Longest Line:")
print(longest)

file.close()