text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("\nCharacter\tFrequency")

for key in freq:
    print(key, "\t\t", freq[key])