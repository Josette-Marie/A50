# Sum of elements in jagged_array

def sum_jagged_array(array):
  total_sum = 0
  for element in array:
    if isinstance(element, int):
      # Add individual numbers
      total_sum += element
    elif isinstance(element, list):
      # Recursively sum nested arrays
      total_sum += sum_jagged_array(element)
    else:
      # Ignore non-numeric elements
      pass

  return total_sum

# Sample Example 
jagged_array = [[1, 2, 3], [4, [5, 6]], 7, [8, 9, [10, 11]]]
total_sum = sum_jagged_array(jagged_array)

print(total_sum)
