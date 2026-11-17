numbers = [10, 15, 20, 25, 30]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even numbers:", count)