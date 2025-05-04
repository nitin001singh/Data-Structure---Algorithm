def plusMinus(arr):
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    n = len(arr)
    
    for value in arr:
        if value < 0:
            negativeCount += 1
        elif value > 0 :
            positiveCount += 1
        else:
            zeroCount += 1
            
    print( round(positiveCount / n , 6),  end="\n" )
    print(round(negativeCount / n, 6), end="\n")
    print(round(zeroCount / n , 6), end="\n")
    
    
res = plusMinus([1,1,0,-1,-1])
print(res)