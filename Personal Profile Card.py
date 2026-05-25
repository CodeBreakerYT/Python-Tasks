# Task 1 - Personal Profile Card

# taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
fav_subject = input("Enter your favourite subject: ")

# calculating birth year
birth_year = 2024 - age

# displaying profile card
print("\nPROFILE CARD")
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Favourite Subject :", fav_subject)
print("Birth Year :", birth_year)
