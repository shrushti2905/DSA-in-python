# Count the number of spaces present in a string.

text = "Python is easy to learn"
count = 0

for ch in text:
    if ch == " ":
        count += 1

print("Total spaces:", count)