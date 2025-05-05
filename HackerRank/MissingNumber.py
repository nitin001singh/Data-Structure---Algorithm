from collections import Counter

def missingNumbers(arr, brr):
    # Write your code here
    c1 = Counter(arr)
    c2 = Counter(brr)
    return sorted(c2 - c1)

# res = missingNumbers([11 ,4 ,11, 7 ,13 ,4 ,12 ,11 ,10 ,14], [11, 4 ,11 ,7 ,3, 7, 10, 13 ,4 ,8 ,12, 11, 10, 14 ,12])
res = missingNumbers([203 ,204 ,205 ,206 ,207 ,208 ,203 ,204 ,205 ,206], [203 ,204 ,204 ,205, 206 ,207 ,205 ,208 ,203 ,206 ,205 ,206 ,204])
print(res)
