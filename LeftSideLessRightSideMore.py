import sys
class Solution:
    def answer(self, nums):
        n = len(nums)
        leftMax   = [0] * n
        rightMin  = [0] * n
        leftMax[0] = -sys.maxsize-1
        rightMin[n-1] = sys.maxsize
        
        for index in range(1, n):
            leftMax[index] = max(nums[index - 1], leftMax[index-1])

        for index in range(n-2, -1, -1):
            rightMin[index] = min(nums[index + 1], rightMin[index + 1 ])
            
        for index in range(1, n-1):
            if  leftMax[index] < nums[index] < rightMin[index]:
                return nums[index]
            
        return -1
        
    
result = Solution().answer([100,200,300])
print(result)