fn = input("Enter filename: ")

try:
    f = open(fn, "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")