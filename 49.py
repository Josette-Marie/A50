# Shuffle an array of strings

import random

def shuffle_strings(strings):
  random.shuffle(strings)

  return strings


strings = ["apple", "banana", "cherry", "grapefruit", "kiwi"]

shuffled_strings = shuffle_strings(strings)

print(shuffled_strings)
