# Bubule Sort
def bubbleSort(arr, n):
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubbleSort(arr, n-1)

# Test the implementation with an example list
arr = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting: ", arr)
print("After sorting: ", bubbleSort(arr, len(arr)))