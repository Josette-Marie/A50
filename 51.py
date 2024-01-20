# Frquency of Letters in a text
def letter_frequencies(text):
  # Create a dictionary to store letter counts
  letter_counts = {}
  for char in text.lower():
    if char.isalpha():
      # Increment the count for the current letter
      letter_counts.setdefault(char, 0)
      letter_counts[char] += 1

  # Convert the dictionary to an array of arrays
  frequencies = [[letter, count] for letter, count in letter_counts.items()]

  # Sort the frequencies by letter (case-insensitive)
  frequencies.sort(key=lambda x: x[0].lower())

  return frequencies

text = "This is a sample text with repeated letters."
frequencies = letter_frequencies(text)

print(frequencies)
