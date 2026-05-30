# Assignment 1 - Tax Calculator

inc = float(input("Enter income: "))

tax = 0

if inc <= 250000:
    tax = 0

elif inc <= 500000:
    tax = (inc - 250000) * 0.05

elif inc <= 1000000:
    tax = 12500 + (inc - 500000) * 0.2

else:
    tax = 112500 + (inc - 1000000) * 0.3

print("Tax :", round(tax, 2))