# Convert Binary String to number

def binary_to_decimal(binary_string):
  # Check for invalid characters
  if not all(char in "01" for char in binary_string):
    raise ValueError("Invalid binary string. Only '0' and '1' allowed.")

  # Calculate the decimal value
  decimal_value = 0
  for i, digit in enumerate(binary_string[::-1]):  # Iterate from right to left
    decimal_value += int(digit) * 2**i  # Apply positional weighting

  return decimal_value


binary_number = "10101"
decimal_value = binary_to_decimal(binary_number)

print(decimal_value)
