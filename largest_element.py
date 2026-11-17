numbers = [15, 40, 25, 60, 10]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)