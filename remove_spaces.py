# Remove all spaces from a string without using replace().

text = "Python is very interesting"
result = ""

for ch in text:
    if ch != " ":
        result += ch

print("Updated string:", result)