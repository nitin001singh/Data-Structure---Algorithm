MOD = 1000000007
MAXN = 100000

fact = [1] * (MAXN + 1)
ifact = [1] * (MAXN + 1)

# Function to compute (base^exp) % MOD using Binary Exponentiation
def power(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Precompute Factorial and Inverse Factorial
def precompute():
    for i in range(1, MAXN + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    ifact[MAXN] = power(fact[MAXN], MOD - 2, MOD)  # Fermat's theorem
    for i in range(MAXN - 1, 0, -1):
        ifact[i] = (ifact[i + 1] * (i + 1)) % MOD

# Compute nCr % MOD
def nCr(n, r):
    if r > n or r < 0:
        return 0
    return (fact[n] * ifact[r] % MOD) * ifact[n - r] % MOD

# Main function
if __name__ == "__main__":
    precompute()
    t = int(input())
    for _ in range(t):
        n, r = map(int, input().split())
        print(nCr(n, r))
