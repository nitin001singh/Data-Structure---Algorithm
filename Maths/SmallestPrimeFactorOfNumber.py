MAXN = 1000000
spf = [i for i in range(MAXN + 1)]  # spf[i] will store the smallest prime factor of i

# Function to compute the smallest prime factors for all numbers up to MAXN
def compute_spf():
    # Start the sieve process
    for i in range(2, int(MAXN**0.5) + 1):
        if spf[i] == i:  # Check if i is prime
            for j in range(i * i, MAXN + 1, i):
                if spf[j] == j:  # Update spf[j] to the smallest prime factor
                    spf[j] = i

# Compute SPF for all numbers from 2 to MAXN
compute_spf()

# Example: Print the smallest prime factor for the first 20 numbers
for i in range(2, 21):
    print(f"Smallest prime factor of {i} is {spf[i]}")
