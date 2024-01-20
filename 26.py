# Return the element in first array not found in second array
def elements_in_first_array_but_not_second(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    result = list(set1 - set2)
    return result

# Example usage
array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
result_array = elements_in_first_array_but_not_second(array1, array2)
print(result_array)
