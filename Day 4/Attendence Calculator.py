# Assignment 2 - Attendance Calculator

td = int(input("Total classes: "))
ad = int(input("Classes attended: "))

per = (ad / td) * 100

print("\nAttendance % :", round(per, 2))

if per >= 75:
    print("Eligible")

else:
    req = int((0.75 * td - ad) / 0.25)

    print("Not Eligible")
    print("Need", req, "more classes")