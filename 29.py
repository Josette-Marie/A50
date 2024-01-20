# Calculating Distance between 100 Prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def calculate_distances(primes):
    distances = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    return distances

# Get the first 100 prime numbers
first_100_primes = get_first_n_primes(100)

# Calculate the distances between consecutive prime numbers
distances = calculate_distances(first_100_primes)

# Print the distances between the first 100 prime numbers
print("Distances between the first 100 prime numbers:", distances)
