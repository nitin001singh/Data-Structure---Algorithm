class Solution:
    def answer(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1 , right + 1]
            
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1 
        

result = Solution().answer( [2,7,11,15], 9) 
print(result)   
