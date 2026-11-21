# Count how many times an element appears in a list.

arr = [10, 20, 30, 20, 40, 20]
target = 20

count = 0

for num in arr:
    if num == target:
        count += 1

print("Occurrences:", count)