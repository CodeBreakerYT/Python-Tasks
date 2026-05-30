bal = 5000

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Balance")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        amt = int(input("Amount: "))
        bal += amt

    elif ch == 2:
        amt = int(input("Amount: "))
        if amt <= bal:
            bal -= amt
        else:
            print("Insufficient Balance")

    elif ch == 3:
        print("Balance =", bal)

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")