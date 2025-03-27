class Practise:
    def resp (self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        biggestLeft = [1] * n
        biggestRight = [1] * n
        
        maxL = 0
        maxR = 0
        waterCount = 0
        
        for index in range(n):
            biggestLeft[index] = maxL
            maxL = max(biggestLeft[index], nums[index])
            
            rightIndex = n - index - 1
            biggestRight[rightIndex] = maxR
            maxR = max(biggestRight[rightIndex], nums[rightIndex] )
            
        # print(biggestLeft, biggestRight)
        
        for index in range(len(nums)):
            minLevel = min(biggestLeft[index], biggestRight[index]) 
            if minLevel > nums[index]:
                waterCount += min(biggestLeft[index], biggestRight[index]) - nums[index]
            
        return waterCount
                
            
            

    
result = Practise().resp([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)