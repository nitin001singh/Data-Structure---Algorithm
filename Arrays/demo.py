class Solution:
    def answer(self , nums, k):
        
        nums.sort()
        left = 0
        right = len(nums) - 1
        maxCount = 0
        while left < right:
            
            if nums[left] + nums[right] == k:
                maxCount += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
                
        return maxCount 
        
        
        
        
         
result = Solution().answer( [-1,0,1,2,-1,-4] )
print(result)
