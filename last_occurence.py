# Find the last occurrence of an element in a list.

arr = [10, 20, 30, 20, 40, 20]
target = 20

position = -1

for i in range(len(arr)):
    if arr[i] == target:
        position = i

print("Last occurrence:", position)