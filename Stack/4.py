# Reverse a List using Stack

arr = [10, 20, 30, 40, 50]
stack = []

for num in arr:
    stack.append(num)

result = []

while stack:
    result.append(stack.pop())

print("Reversed List:", result)