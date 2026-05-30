def ctof(c):
    return (c * 9 / 5) + 32

c = float(input("Enter temperature in Celsius: "))

print("Fahrenheit =", ctof(c))