def hurdleRace(k, height):
    maxElem = max(height)
    if maxElem < k:
        return 0
    else:
        return maxElem - k
    

res = hurdleRace(7,[2,5,4,5,2])
print(res)
