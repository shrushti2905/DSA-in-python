# Find all positions of a given element in a list.

arr = [5, 10, 5, 20, 5, 30]
target = 5

positions = []

for i in range(len(arr)):
    if arr[i] == target:
        positions.append(i)

print("Positions:", positions)