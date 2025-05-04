def birthdayCakeCandles(candles):
    # Write your code here
    maxVal = max(candles)
    totalCount = 0
    for value in candles:
        if value >= maxVal:
            maxVal = value
            totalCount += 1
    
    # for value in candles:
    #     if value == maxVal:
    #         totalCount += 1
            
    return totalCount


res = birthdayCakeCandles([18 ,90, 90, 13, 90, 75, 90, 8 ,90, 43])
print(res)