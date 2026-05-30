def valid(p):
    if len(p) >= 8:
        return True
    return False

p = input("Enter password: ")

if valid(p):
    print("Valid Password")
else:
    print("Invalid Password")