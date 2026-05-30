n = int(input("Enter number: "))

if n < 2:
    print("Not Prime")
else:
    f = 0

    for i in range(2, n):
        if n % i == 0:
            f = 1
            break

    if f == 1:
        print("Not Prime")
    else:
        print("Prime")