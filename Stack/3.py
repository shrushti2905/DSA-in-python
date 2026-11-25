# Reverse a String using Stack

text = "python"
stack = []

for char in text:
    stack.append(char)

result = ""

while stack:
    result += stack.pop()

print("Reversed String:", result)