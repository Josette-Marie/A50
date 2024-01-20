# Find Maximum in a jagged array

def find_max_in_jagged_array(array):
  max_value = float('-inf')  # Initialize with negative infinity to handle any numbers

  for element in array:
    if isinstance(element, int):
      # Compare individual numbers with the current maximum
      max_value = max(max_value, element)
    elif isinstance(element, list):
      # Recursively find the maximum in nested arrays and compare
      max_value = max(max_value, find_max_in_jagged_array(element))

  return max_value

# Sample Example
jagged_array = [[1, 2, 3], [4, [5, 6]], 7, [8, 9, [10, 11]]]
max_number = find_max_in_jagged_array(jagged_array)

print(max_number)
