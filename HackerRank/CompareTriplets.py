def compareTriplets(a, b):
    aliceCount = 0
    bobCount = 0
    for index in range(len(a)):
        if a[index] > b[index]:
            aliceCount += 1
        elif a[index] < b[index]:
            bobCount += 1
            
    return [aliceCount, bobCount]

res = compareTriplets([1, 2, 3], [3, 2, 1])
print(res)