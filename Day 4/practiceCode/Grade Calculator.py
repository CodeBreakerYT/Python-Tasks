def grade(m):
    if m >= 90:
        return "A"
    elif m >= 80:
        return "B"
    elif m >= 70:
        return "C"
    elif m >= 60:
        return "D"
    else:
        return "F"

m = int(input("Enter marks: "))

print("Grade =", grade(m))