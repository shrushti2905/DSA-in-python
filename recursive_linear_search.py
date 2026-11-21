# Search for an element using recursive linear search.

def search(arr, target, index):
    if index == len(arr):
        return -1

    if arr[index] == target:
        return index

    return search(arr, target, index + 1)


arr = [10, 20, 30, 40, 50]
print(search(arr, 40, 0))