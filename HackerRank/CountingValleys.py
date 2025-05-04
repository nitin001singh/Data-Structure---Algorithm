def countingValleys(steps, path):
    # Write your code here
    up = 0
    down = 0
    totalCount = 0
    for x in path:
        if x == "U":
             up += 1
             if up == down:
                totalCount += 1
        else:
            down += 1

    return totalCount
            
    
res = countingValleys(12, ['D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D'])
print(res)                              
