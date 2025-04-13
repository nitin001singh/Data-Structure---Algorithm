class Solution:
    def answer(self, nums):
        if len(nums) < 1:
            return 0
        
        hashset= set()
        left = 0 
        right = 1
        maxCount = 1
        hashset.add(nums[0])
        
        while right < len(nums):
            while nums[right] in hashset:
                hashset.remove(nums[left])
                left += 1
            
            hashset.add(nums[right])
            right += 1
            maxCount = max(maxCount, right - left )
            
                
        return maxCount
        
result = Solution().answer(  "pwwkew" )  
print(result)   
