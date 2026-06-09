def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

print("Simple Interest =", simple_interest(p, r, t))