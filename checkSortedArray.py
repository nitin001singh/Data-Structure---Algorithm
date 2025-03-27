class Solution:
    def checkSortedArray(self, nums):
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                return False
        return True
    
    
result = Solution().checkSortedArray([1,2,3,4])
print(result)