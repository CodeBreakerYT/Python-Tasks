basic = float(input("Enter Basic Salary: "))

hra = basic * 20 / 100
da = basic * 10 / 100

gross_salary = basic + hra + da

print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross_salary)