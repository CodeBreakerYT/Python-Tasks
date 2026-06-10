source = open("student.txt", "r")

data = source.read()

destination = open("copy.txt", "w")

destination.write(data)

source.close()
destination.close()

print("Copied Successfully")