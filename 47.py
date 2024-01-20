# Copy jagged array with numbers or other numbers from other array
import copy

def deep_copy_jagged_array(array):
  copy_array = copy.deepcopy(array)

  return copy_array

original_array = [[1, 2, 3], [4, [5, 6]], 7, [8, 9, [10, 11]]]
copied_array = deep_copy_jagged_array(original_array)

# Modify the copied array
copied_array[1][1][0] = 100

print(original_array) 
print(copied_array) 
