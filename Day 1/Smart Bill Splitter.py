# Task 2 - Smart Bill Splitter

# taking user input
b = float(input("Enter total bill amount: "))
p = int(input("Enter number of people: "))
t = float(input("Enter tip percentage: "))

# arithmetic operators
ta = (b * t) / 100      # tip amount
tb = b + ta             # total bill
dc = tb - 50            # discount check
app = tb / p            # amount per person
r = round(tb % p)       # rounded remainder

# rounding values
tb = round(tb, 2)
app = round(app, 2)

# displaying result
print("\nBILL SUMMARY")
print("Total Bill :", format(tb, ".2f"))
print("Amount Per Person :", format(app, ".2f"))
print("Remaining Amount After Split :", format(r, ".2f"))