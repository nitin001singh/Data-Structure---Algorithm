def closestNumber(arr):
    arr.sort()
    res = []
    pairs = {}
 
    for i in range(0, len(arr) - 1):
        pairs[i] = abs(arr[i] - arr[i+1])
        
    min_diff = min(pairs.values())

    for k, v in pairs.items():
        if v == min_diff:
            res.append(arr[k])
            res.append(arr[k + 1])
 
    return res    
res = closestNumber([-20 ,-3916237, -357920 ,-3620601 ,7374819 ,-7330761 ,30, 6246457, -6461594 ,266854])
print(res)

