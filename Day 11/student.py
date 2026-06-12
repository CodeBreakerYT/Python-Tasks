import csv

file = open("student.csv", "r")

reader = csv.reader(file)

next(reader)     # Skip header

highest = 0
topper = ""

total_marks = 0
count = 0

print("\nSTUDENT RECORDS\n")

print(
f"{'RollNo':<8}{'Name':<10}{'Physics':<10}{'Chemistry':<12}{'Maths':<8}{'English':<8}{'Total'}"
)

for row in reader:

    print(
        f"{row[0]:<8}"
        f"{row[1]:<10}"
        f"{row[2]:<10}"
        f"{row[3]:<12}"
        f"{row[4]:<8}"
        f"{row[5]:<8}"
        f"{row[6]}"
    )

    total = int(row[6])

    total_marks += total
    count += 1

    if total > highest:
        highest = total
        topper = row[1]

file.close()


average = total_marks / count

print("\nTopper =", topper)
print("Highest Marks =", highest)
print("Average Marks =", round(average, 2))