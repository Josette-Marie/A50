# Compose a new from two aothers 

def symmetric_difference_array(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    result = list((set1 - set2) | (set2 - set1))
    return result

# Sample test
array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
result_array = symmetric_difference_array(array1, array2)
print(result_array)