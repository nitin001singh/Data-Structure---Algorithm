# Optimal

# TC : O(N)
# SC : O(1)

class Solution:
    def answer(self , nums):
        n = len(nums) - 1
        breakPoint = -1
        for index in range(n-1, -1, -1):
            if nums[index] < nums[index+1]:
                breakPoint = index
                break
            
        if breakPoint == -1:
            return nums[::-1]

        for index in range(n, breakPoint  , -1):
            if nums[index] > nums[breakPoint]:
                nums[breakPoint], nums[index] = nums[index], nums[breakPoint]
                break
            
        nums[breakPoint+1:] = nums[breakPoint + 1 :][::-1]
        return nums
    
    
result = Solution().answer([3,2,1])
print(result)