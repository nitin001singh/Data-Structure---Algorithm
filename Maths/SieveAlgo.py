import math

# Function to find all prime numbers up to n using the Sieve of Eratosthenes
def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

    limit = int(math.sqrt(n))
    for p in range(2, limit + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    primes = [i for i in range(n + 1) if prime[i]]
    return primes

# Function to find primes in a range [start, end] using a segmented sieve
def sieve_range(start, end):
    primes = sieve(end)
    range_primes = [p for p in primes if p >= start]
    return range_primes

# Driver code
if __name__ == "__main__":
    l = 1  # Start of range
    r = 100  # End of range

    primes_in_range = sieve_range(l, r)

    # Print all prime numbers in the range
    for prime in primes_in_range:
        print(prime)
