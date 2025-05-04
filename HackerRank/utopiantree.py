def utopian(n):
    ans = 1
    for val in range(1,n+1):
        if val % 2 != 0:
            ans *= 2
        else:
            ans += 1
    return ans

        
res = utopian(3)
print(res)                              
