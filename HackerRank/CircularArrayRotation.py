def circularRotation(a, k , queries):
    
    k = k % len(a)
    ans = []
    for i in range(k):
        las = a.pop(-1)
        a.insert(0,las)
    for i in queries:
        ans.append(a[i]) 
    return ans   
    
res = circularRotation([3,4,5],2,[1,2])
print(res)                              


# 3 4 5
# 5 3 4
# 4 5 3