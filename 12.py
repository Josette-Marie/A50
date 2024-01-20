# Return all positive numbers in the array

def GetPositiveNumber(array):
    array2 = []
    for i in array:
        if i >= 0:
            array2.append(i)

    return array2


array = [2,3,4,5,-1]
print(GetPositiveNumber(array))
            
