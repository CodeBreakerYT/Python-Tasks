def eo(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter number: "))

print(eo(n))