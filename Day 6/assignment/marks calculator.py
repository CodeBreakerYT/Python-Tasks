# BUG 1 - RUNTIME ERROR

# Type  : ZeroDivisionError
# Cause : Average calculated using len(marks) before any marks are added
# Fix   : Take all inputs first, then calculate average

# BUGGY CODE

# marks = []
# avg = sum(marks) / len(marks)

# FIXED CODE

marks = []

for i in range(5):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)


# BUG 2 - LOGICAL ERROR

# Type  : Logical Error
# Cause : Highest and Lowest marks assigned incorrectly
# Fix   : Use max() for highest and min() for lowest

# BUGGY CODE

# high = min(marks)
# low = max(marks)

# FIXED CODE

total = sum(marks)
avg = total / len(marks)
high = max(marks)
low = min(marks)

print("\nTotal Marks =", total)
print("Average Marks =", avg)
print("Highest Marks =", high)
print("Lowest Marks =", low)