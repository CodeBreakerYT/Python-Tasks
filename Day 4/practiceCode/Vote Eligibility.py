def vote(a):
    return a >= 18

a = int(input("Enter age: "))

if vote(a):
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")