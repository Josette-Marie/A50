# Rotating an array to the left position

def RotatingToLeft(array):
    k = len(array)
    temp = array[k -1]

    for i in range(k - 1,0,-1):
        array[i] = array[i-1]
    array[0] = temp
    return array

array = ["c", "a","r"]
print(RotatingToLeft(array))
