
# Optimal 

# TC : O(N)
# SC : O(1)

class Solution:
    def answer(self, nums):
        left = 0
        mid = 0
        right = len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
    
        return nums
    
    
result = Solution().answer([2,0,2,1,1,0] )
print(result)