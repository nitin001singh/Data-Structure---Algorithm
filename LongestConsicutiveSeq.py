# Brute force 

# TC : O(N^2)
# SC : O(n)

# class Solution:
#     def answer(self, nums):
#         nums = sorted(nums)
#         # print(nums)
#         maxCount = 0
        
#         for value in nums:
#             tempCount = 1
#             while value + 1 in nums:
#                 tempCount += 1
#                 value += 1

#             maxCount = max(maxCount, tempCount)
            
#         return maxCount
                
        
# result = Solution().answer(  [1,0,1,2] )  
# print(result)   


# Brute force 

# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self, nums):
#         if len(nums) < 1:
#             return 0
        
#         maxLen = 0
#         for index in range(len(nums)):
#             currentNum = nums[index]
#             currentLen = 1
            
#             while currentNum + 1 in nums:
#                 currentNum = currentNum + 1
#                 currentLen += 1
                
#             maxLen = max(maxLen , currentLen)
            
#         return maxLen
            
        


# result = Solution().answer( [100,4,200,1,3,2] ) 
# print(result)   

# Optimal 
# TC : O(n)
# SC : O(n)

class Solution:
    def answer(self, nums):
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
                
        
result = Solution().answer(  [100,4,200,1,3,2] )  
print(result)   
  