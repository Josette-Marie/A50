# Rotating an array to the right position

def RotatingToLeft(array):
    k = len(array)
    temp = array[0]

    for i in range(k - 1):
        array[i] = array[i+1]
    array[k - 1] = temp
    return array

array = ["c", "a","r"]
print(RotatingToLeft(array))
