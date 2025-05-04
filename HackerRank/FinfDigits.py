def findDigits(n):
    totalCount = 0
    number = n
    while number > 0:
        remainder = number % 10
        if remainder and (n % remainder == 0):
            # print(remainder)
            totalCount += 1
        
        number //= 10
    return totalCount
   
res = findDigits(22)
print(res) 