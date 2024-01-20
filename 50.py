# Fiil Array randomly from 1 to n
import random

def generate_unique_random_numbers(n):
  numbers = list(range(1, n + 1))
  random.shuffle(numbers) 

  return numbers[:n]

n = 10
random_numbers = generate_unique_random_numbers(n)

print(random_numbers)
