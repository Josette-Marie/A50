# Fib(500) wuth high precision

from decimal import Decimal, getcontext

getcontext().prec = 1000  # Set precision to 1000 decimal places

def fibonacci(n):
  if n <= 2:
    return n
  else:
    a, b = Decimal(1), Decimal(1)
    for _ in range(3, n + 1):
      c = a + b
      a, b = b, c
    return c

result = fibonacci(500)
print(result)
