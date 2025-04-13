# Brute Force 

# TC : O(N)
# SC : O(N)

# class Solution :
#     def maxConsecutive(self, nums):
#         n = len(nums)
#         frqArr = [0] * n
#         start = 0
#         for index in range(len(nums)):
#             if nums[index] == 1:
#                 frqArr[start] += 1
#             else:
#                 start += 1
                
#         return max(frqArr)
                  

# result = Solution().maxConsecutive([0,0,1 ,1 ,1 ,1, 0,1,1 , 0, 1, 1, 1,1,1,0,0,0,1,1,1,0,1,1,1,1])
# print(result)


# Optimized 
# TC : O(N)
# SC : O(1)

class OptimizeSolution :
    def maxConsecutive(self, nums):
        maxCount = 0
        currentCount = 0
        for value in nums:
            if value == 1:
                currentCount += 1
                maxCount = max(maxCount, currentCount)
            else:
                currentCount = 0
                
        return maxCount
                  

result = OptimizeSolution().maxConsecutive([0,0,1 ,1 ,1 ,1, 0,1,1 , 0, 1, 1, 1,1,1,0,0,0,1,1,1,0,1,1,1,1])
print(result)