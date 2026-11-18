# Count the total number of consonants in a string.

text = "Hello Python"
count = 0

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Total consonants:", count)