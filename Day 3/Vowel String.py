# Vowel String

word = "PYTHON"

# Character by character
for ch in word:
    print(ch, end="-")      # P-Y-T-H-O-N-

print()

# Check vowels
vow = "AEIOU"

for ch in word:

    if ch in vow:
        print(f"{ch} is a vowel")