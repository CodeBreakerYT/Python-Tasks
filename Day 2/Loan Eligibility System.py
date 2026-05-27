# Task 1 - Enhanced Loan Eligibility System

age = int(input("Enter age: "))
sal = int(input("Enter salary: "))
emp = input("Enter employment type: ").lower()

if age < 21 or age > 60:
    print("Rejected: Age not eligible")

elif sal < 25000:
    print("Rejected: Salary too low")

elif emp != "salaried" and emp != "self-employed":
    print("Rejected: Invalid employment type")

elif age >= 21 and age <= 30 and sal < 30000:
    print("Needs guarantor")

elif age > 55 and emp == "self-employed":
    print("High risk, senior review needed")

else:
    print("Approved")