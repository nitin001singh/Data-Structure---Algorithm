class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if not nums :
        #     return []
        # n = len(nums)
        # temp = [0] * n
        
        # for index in range(1 , n):
        #     temp[index - 1] = nums[index]
            
        # temp[n-1] = nums[0]
        # return temp
        
        
        if not nums :
            return []
        n = len(nums)
        firstVal = nums[0]
        for index in range(1 , n):            
            nums[index - 1] = nums[index]        
        nums[n - 1] = firstVal
        
        return nums
        
        
    
result = Solution().rotate([-1,-100,3,99],2)
print(result)