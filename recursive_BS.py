# Search for an element using recursive binary search in a sorted list.

def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)

    return binary_search(arr, target, mid + 1, high)


arr = [10, 20, 30, 40, 50, 60]
print(binary_search(arr, 40, 0, len(arr) - 1))