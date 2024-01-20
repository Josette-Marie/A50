# Extract column from bi dimesional array

def extract_column(array, column_index):
  # Check for valid column index
  if column_index < 0 or column_index >= len(array[0]):
    raise IndexError("Invalid column index.")

  # Extract the elements of the specified column
  column = [row[column_index] for row in array]

  return column

# Sample Example
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
extracted_column = extract_column(array, 1)  # Extract the second column

print(extracted_column)  # Output: [2, 5, 8]
