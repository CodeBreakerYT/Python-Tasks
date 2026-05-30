# Return Values in Python Functions

# Single Return Value
def square(n):
    return n * n

# Multiple Return Values
def min_max(lst):
    return min(lst), max(lst)

# Return Dictionary
def stats(lst):
    return {
        "mean": sum(lst) / len(lst),
        "min": min(lst),
        "max": max(lst),
        "count": len(lst)
    }

n = int(input("Enter a number: "))

print("Square =", square(n))

nums = [5, 2, 9, 1, 7]

lo, hi = min_max(nums)

print("Minimum =", lo)
print("Maximum =", hi)

data = [10, 20, 30, 40]

res = stats(data)

print("Mean =", res["mean"])
print("Min =", res["min"])
print("Max =", res["max"])
print("Count =", res["count"])