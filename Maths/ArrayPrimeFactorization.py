import math
from collections import defaultdict

MAXN = 1000000

# Array to store the smallest prime factor for each number
spf = [i for i in range(MAXN + 1)]

# Function to compute the Smallest Prime Factor (SPF) for all numbers up to MAXN
def compute_spf():
    for i in range(2, int(math.sqrt(MAXN)) + 1):
        if spf[i] == i:  # i is a prime number
            for j in range(i * i, MAXN + 1, i):
                if spf[j] == j:  # Update spf[j] to the smallest prime factor
                    spf[j] = i

# Function to get prime factorization of a number using the precomputed SPF
def get_prime_factors(num):
    factors = defaultdict(int)
    while num != 1:
        prime = spf[num]
        factors[prime] += 1
        num //= prime
    return factors

def main():
    n = int(input())  # Read the size of the array
    b = list(map(int, input().split()))  # Input the array of numbers
    
    # Compute SPF for all numbers from 2 to MAXN
    compute_spf()
    
    # Process each number in the array and print its prime factorization
    for i in range(n):
        num = b[i]
        prime_factors = get_prime_factors(num)
        
        # Output the prime factorization for b[i]
        print(f"Prime factorization for b[{i+1}] = {num} :", end=" ")
        for prime, count in prime_factors.items():
            print(f"{prime}^{count}", end=" ")
        print()  # Newline after each prime factorization

if __name__ == "__main__":
    main()