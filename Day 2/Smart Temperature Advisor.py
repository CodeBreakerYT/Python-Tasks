# Task 2 - Smart Temperature Advisor

t = int(input("Enter temperature: "))

if t < 0:
    print("Freezing! Stay indoors and wear heavy clothing")

elif t <= 15:
    print("Cold. A jacket is recommended")

elif t <= 25:
    print("Pleasant weather! Great for outdoor activities")

elif t <= 35:
    print("Hot. Stay hydrated and use sunscreen")

else:
    print("Extreme heat! Avoid going outside")