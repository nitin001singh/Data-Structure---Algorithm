# Tc : O(N)
# Sc : O(N)

class Solution:
    def answer(self, nums):
        if not nums:
            return 0

        hashSet = set(nums)
        maxCount = 0
        
        for value in hashSet:
            if value - 1 not in hashSet:
                currentNum = value
                tempCount = 1
                while currentNum + 1 in hashSet:
                    tempCount += 1
                    currentNum += 1

                maxCount = max(maxCount, tempCount)
            
        return maxCount
    
    
    
res=  Solution().answer([100,4,200,1,3,2])
print(res)