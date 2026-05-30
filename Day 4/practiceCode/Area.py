def rect(l, b):
    return l * b

def circ(r):
    return 3.14 * r * r

ch = int(input("1.Rectangle \n2.Circle \nEnter choice: "))

if ch == 1:
    l = float(input("Length: "))
    b = float(input("Breadth: "))
    print("Area =", rect(l, b))

elif ch == 2:
    r = float(input("Radius: "))
    print("Area =", circ(r))

else:
    print("Invalid Choice")