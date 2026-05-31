# List Comprehension to Generate Squares

n = int(input("Enter a number: "))

squares = [x**2 for x in range(1, n + 1)]

print("Squares:", squares)