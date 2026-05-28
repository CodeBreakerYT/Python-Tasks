# Task 2 - Production Counter System

import random

# input
tg = int(input("Target units: "))
wk = int(input("Workers per shift: "))
df = float(input("Defect %: "))

tt = 0

# 3 shifts
for s in range(1, 4):

    pd = 0
    dc = 0

    print("\nShift", s)

    # 20 machine cycles
    for c in range(1, 21):

        # stop if target reached
        if tt >= tg:
            break

        x = random.randint(1, 100)

        # defective item
        if x <= df:
            dc += 1
            continue

        # good product
        pd += 1
        tt += 1

    # worker productivity
    pr = pd / wk

    print("Produced :", pd)
    print("Defects  :", dc)
    print("Productivity :", round(pr, 2))

    # stop all production
    if tt >= tg:
        print("\nTarget Reached")
        break

print("\nTotal Produced :", tt)