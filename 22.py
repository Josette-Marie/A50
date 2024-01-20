# Reverse an array

def ReverseArr(array):
    arr = []
    for i in range(len(array) - 1, -1, -1):
        arr.append(array[i])
    return arr

array = [1,2,3,4,5]
print(ReverseArr(array))
