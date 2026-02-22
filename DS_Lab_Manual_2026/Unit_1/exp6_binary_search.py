def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)

arr = [2,4,6,8,10,12]
key = 8

result = binary_search(arr, key, 0, len(arr)-1)
print("Index:", result)