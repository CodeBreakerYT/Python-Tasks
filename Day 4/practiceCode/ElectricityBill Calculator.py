def bill(u):
    if u <= 100:
        return u * 2
    elif u <= 200:
        return 100 * 2 + (u - 100) * 3
    else:
        return 100 * 2 + 100 * 3 + (u - 200) * 5

u = int(input("Enter units: "))

print("Bill =", bill(u))