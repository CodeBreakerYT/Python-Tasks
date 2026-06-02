a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    print("Result =", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")