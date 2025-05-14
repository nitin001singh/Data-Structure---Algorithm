import math

def print_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                divisors.append(i)  # Only one occurrence if both are the same
            else:
                divisors.append(i)  # Add the smaller divisor
                divisors.append(n // i)  # Add the larger divisor
    return divisors

# Example usage
n = 12
divisors = print_divisors(n)
divisors.sort(reverse=True)  # Sort divisors in descending order

print(" ".join(map(str, divisors)))
