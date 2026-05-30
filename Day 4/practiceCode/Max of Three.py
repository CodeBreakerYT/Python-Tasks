def mx(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum =", mx(a, b, c))