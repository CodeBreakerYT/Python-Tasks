import pickle

file = open("employee.dat", "wb")

records = []

for i in range(2):
    empid = int(input("Enter ID: "))
    name = input("Enter Name: ")

    records.append([empid, name])

pickle.dump(records, file)

file.close()

file = open("employee.dat", "rb")

data = pickle.load(file)

search = int(input("Search ID: "))

for record in data:

    if record[0] == search:
        print("Found:", record)

file.close()