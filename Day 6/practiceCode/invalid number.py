try:
    n = int(input("Enter a number: "))
    print("You entered:", n)
except ValueError:
    print("Invalid input. Please enter a number.")