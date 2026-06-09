numbers = [12, 7, 18, 9, 24, 31]

count = 0

for i in numbers:
    if i % 2 == 0:
        count += 1

print("Even Numbers Count =", count)