# Return 100 prime numbers 
 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def calculate_sum(arr):
    return sum(arr)

# Get the first 100 prime numbers
first_100_primes = sum_of_first_n_primes(100)

# Calculate the sum of the first 100 prime numbers
sum_of_primes = calculate_sum(first_100_primes)

# Return the sum of the first 100 prime numbers and the array of prime numbers
print("Sum of the first 100 prime numbers:", sum_of_primes)
print("Array of the first 100 prime numbers:", first_100_primes)
