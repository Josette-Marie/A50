# Convert ASCII Code to String
def ascii_codes_to_string(ascii_codes):
  return "".join(chr(code) for code in ascii_codes)

test_codes = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
original_string = ascii_codes_to_string(test_codes)
print(original_string)

