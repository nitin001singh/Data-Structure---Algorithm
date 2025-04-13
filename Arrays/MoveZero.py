# Optimal 

# TC : O(N)
# SC : O(1)

class Solution:
    def moveZero(self, nums):
        starting = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[starting], nums[index] = nums[index], nums[starting]
                starting += 1
                
        return nums
            
    
res = Solution().moveZero([1,0,2,0,0,3,4])
print(res)
    