def countApplesAndOranges(s, t, a, b, apples, oranges):

    # totalApples =  [ (a + x) for x in apples ]
    # totalOranges =  [ (b + x) for x in oranges ]
    
    appleCount = 0
    orangeCount = 0
    for x in apples:
        distance = x + a 
        if distance >= s and distance <= t:
            appleCount += 1
            
    for x in oranges:
        distance = x + b 
        if distance >= s and distance <= t:
            orangeCount += 1
            
    print(appleCount)
    print(orangeCount)
    
    
res = countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
print(res)