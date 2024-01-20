# Convert csv text to bi-dimentional array
import csv

def csv_to_2d_array(csv_text):
  array = []
  reader = csv.reader(csv_text.splitlines())  # Handle newlines effectively
  for row in reader:
    array.append(row)
  return array

csv_text = "Name,Age\njohn, 13\nAnna,26"
array = csv_to_2d_array(csv_text)
print(array)


