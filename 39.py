# Caesar cypher
def caesar_cipher(text, shift, mode="encrypt"):
  result = ""
  for char in text:
    if char.isalpha():
      base = ord('A') if char.isupper() else ord('a')
      new_char_code = (ord(char) - base + shift) % 26 + base
      result += chr(new_char_code)
    else:
      result += char

  return result

encrypted_text = caesar_cipher("Hello, world!", 3, mode="encrypt")
print(encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, 3, mode="decrypt")
print(decrypted_text)
