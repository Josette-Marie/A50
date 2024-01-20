# factorial (70) high precision

def high_precision_factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i 
    
    # Split into chunks of 10 digits to prevent overflow
    while result % 10**10 == 0:
      result //= 10**10

  # Combine remaining chunks
  digits = []
  while result > 0:
    digits.append(result % 10)
    result //= 10

  # Reverse the digits and construct the final number string
  return "".join(str(digit) for digit in digits[::-1])

result = high_precision_factorial(70)
print(result)
