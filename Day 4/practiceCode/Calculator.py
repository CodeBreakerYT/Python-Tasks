def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print(add(a, b))
elif op == "-":
    print(sub(a, b))
elif op == "*":
    print(mul(a, b))
elif op == "/":
    print(div(a, b))
else:
    print("Invalid operator")