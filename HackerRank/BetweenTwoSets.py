def getTotalX(a, b):
    # Write your code here
    count = 0
    for x in range(max(a), min(b)+1):
        if all(x % m == 0 for m in a):
            if all(n % x == 0 for n in b):
                count += 1
    return count
    
    
res = getTotalX([2,6], [24,36])
print(res)