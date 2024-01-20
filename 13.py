# Findin the maximum element in an array

def findMax(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max 

arr = [1,5,4,3,2]
print(findMax(arr))