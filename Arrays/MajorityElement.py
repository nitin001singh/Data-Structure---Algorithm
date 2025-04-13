# Brute Force

# TC : O(N)
# SC : O(N)

# class Solution:
#     def majorityElement(self, nums):
#         maps = {}
#         for value in nums:
#             if value in maps:
#                 maps[value] += 1
#             else:
#                 maps[value] = 1
#         return maps
        
    
# result = Solution().majorityElement([3,2,3])

# maxElem = 0
# freqCount = 0
    
# for value, index in result.items():
#     if value > maxElem:
#         maxElem = value
#         freqCount  = index
        
    
# print(maxElem, freqCount)


# Optimal Solution
# TC : O(N)
# SC : O(1)

class OptimizeSolution:
    def majorityElement(self, nums):
        throne = nums[0]
        freqCount = 1
        for index in range(1, len(nums)):
            if freqCount == 0:
                throne = nums[index]
                freqCount = 1
            
            elif throne == nums[index]:
                freqCount += 1
            else:
                freqCount -= 1          
                
        count = self.getFreqOfNumber(nums, throne)
        if count > len(nums) // 2:
            return throne
        return -1 
    
    def getFreqOfNumber(self, nums, throne):
        numberFreq = 0
        for value in nums:
            if value == throne:
                numberFreq += 1
        return numberFreq
        
     
     
result = OptimizeSolution().majorityElement([3 ,1, 3, 3, 2])
print(result)