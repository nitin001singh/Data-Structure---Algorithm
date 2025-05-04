def acm(topic):
    n = len(topic)
    ans = 0
    hashmap = {}
    for x in range(n): 
        for y in range(x+1, n):
            ans = countTopic(topic[x], topic[y])
            if ans in hashmap:
                hashmap[ans] += 1
            else:
                hashmap[ans] = 1

    opt = []
    maxVal = float("-inf")
    maxIndex = 0
    for value, index in hashmap.items():
        if value > maxVal:
            maxVal = value
            maxIndex = index
    
    opt.append(maxVal)
    opt.append(maxIndex)
    return opt


def countTopic(a,b):
    count = 0
    for x in range(len(a)):
        if a[x] == '1' or b[x] == '1':
            count += 1
    return count
            
    
res = acm(['10101','11100','11010','00101'])
print(res)
