# Return Distinct element in an array

def get_distinct_elements(arr):
    distinct_elements = list(set(arr))
    return distinct_elements

# Example usage
input_array = [1, 2, 2, 3, 4, 4, 5]
result_array = get_distinct_elements(input_array)
print(result_array)
