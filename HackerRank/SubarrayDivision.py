def birthday(s, d, m):
    
    ways = 0
    n = len(s)
    summ = 0
    for x in range(m):
        summ += s[x]
    if summ == d:
        ways += 1
        
    for i in range(m, n):
        summ = (summ - s[i-m])  + s[i]
        # print(summ)
        if summ == d:
            ways += 1
            
    return ways
        
    
    
res = birthday([2,2,1,3,2], 4, 2)
print(res)