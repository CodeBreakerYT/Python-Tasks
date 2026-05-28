# Task 1 - Number Pattern Generator

n = int(input("Enter n: "))

print("\nRight Triangle\n")

for i in range(1, n + 1):
    print("* " * i)

print("\nInverted Number Triangle\n")

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPascal Triangle\n")

for i in range(n):

    print(" " * (n - i), end="")

    v = 1

    for j in range(i + 1):
        print(v, end=" ")

        v = v * (i - j) // (j + 1)

    print()

print("\nPrime Numbers\n")

for i in range(2, n + 1):

    for j in range(2, i):

        if i % j == 0:
            break

    else:
        print(i, end=" ")