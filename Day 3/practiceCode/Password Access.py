pwd = "python123"

for i in range(3):
    p = input("Enter password: ")

    if p == pwd:
        print("Access Granted")
        break
else:
    print("Account Locked")