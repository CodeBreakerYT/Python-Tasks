file = open("result.txt", "w")

for i in range(3):

    name = input("Enter Name: ")
    phy = int(input("Physics: "))
    chem = int(input("Chemistry: "))
    maths = int(input("Maths: "))

    total = phy + chem + maths

    file.write(
        name + "," +
        str(phy) + "," +
        str(chem) + "," +
        str(maths) + "," +
        str(total) + "\n"
    )

file.close()

file = open("result.txt", "r")

topper = ""
highest = 0

for line in file:

    data = line.strip().split(",")

    name = data[0]
    total = int(data[4])

    if total > highest:
        highest = total
        topper = name

print("Topper =", topper)
print("Total =", highest,"/300")

file.close()