def pay(bs):
    hra = bs * 0.2
    da = bs * 0.1
    return bs + hra + da

bs = float(input("Enter basic salary: "))

print("Gross Salary =", pay(bs))