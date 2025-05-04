def missingNumbers(arr, brr):
    # Write your code here
    hashmapArr = {}
    for x in arr:
        if x in hashmapArr:
            hashmapArr[x] += 1
        else:
             hashmapArr[x] = 1
        
    hashmapBrr = {}
    for x in brr:
        if x in hashmapBrr:
            hashmapBrr[x] += 1
        else:
             hashmapBrr[x] = 1
    
    opt = set()
    finalMap = hashmapArr  if len(hashmapArr) > len(hashmapBrr) else hashmapBrr
    for val in finalMap:
        if not hashmapArr.get(val):
            opt.add(val)
            
        if hashmapArr.get(val) != hashmapBrr.get(val):
            opt.add(val)
        
        
    return  opt

res = missingNumbers([11 ,4 ,11, 7 ,13 ,4 ,12 ,11 ,10 ,14], [11, 4 ,11 ,7 ,3, 7, 10, 13 ,4 ,8 ,12, 11, 10, 14 ,12])
# res = missingNumbers([203 ,204 ,205 ,206 ,207 ,208 ,203 ,204 ,205 ,206], [203 ,204 ,204 ,205, 206 ,207 ,205 ,208 ,203 ,206 ,205 ,206 ,204])
print(res)
