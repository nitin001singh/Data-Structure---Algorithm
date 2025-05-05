def salesByMatch(p):
    hashmap = {}
    for x in range(len(p)):
        if p[x] in hashmap:
            hashmap[p[x]] += 1
        else:
            hashmap[p[x]] = 1
            
    
    res = 0
    for index,value in hashmap.items():
        res += (value // 2)
            
    return res

res = salesByMatch([1,2,1,2,1,3,2])
print(res)
