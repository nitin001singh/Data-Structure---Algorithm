import math
from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(int)

    # Count the number of 2s that divide n
    while n % 2 == 0:
        factors[2] += 1
        n //= 2

    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        factors[n] += 1

    return factors

# Driver code
n = 18
factors = prime_factors(n)

# Print prime factors and their counts
for factor, count in factors.items():
    print(f"{factor} {count}")
