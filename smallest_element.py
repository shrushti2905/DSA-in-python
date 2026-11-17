numbers = [15, 40, 25, 60, 10]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)