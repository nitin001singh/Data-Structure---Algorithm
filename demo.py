class Solution:
    def answer(self, nums):
        left = 0
        right = len(nums) - 1
        
        maxCapacity = 0
        
        while left < right:
            width = right - left
            height = min(nums[left], nums[right])
            area = width * height
            maxCapacity = max(maxCapacity, area)
            
            if nums[left] < nums[right]:
                left += 1
            else :
                right -= 1
                
        return maxCapacity             
    
    
result = Solution().answer([1,8,6,2,5,4,8,3,7])
print(result)