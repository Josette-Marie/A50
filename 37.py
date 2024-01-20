# Convert String to ASCII codes
def string_to_ascii_codes(string):
  return [ord(char) for char in string]

test_string = "Hello, world!"
ascii_codes = string_to_ascii_codes(test_string)
print(ascii_codes)
