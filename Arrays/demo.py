class Solution:
    def answer(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        
        if n % 2 == 0:
            return (nums[n//2 - 1] + nums[n//2]) / 2.0 
        else:
            return nums[n//2]

    
result = Solution().answer([1,2], [3,4])
print(result)