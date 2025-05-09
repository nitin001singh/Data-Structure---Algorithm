class Solution:
    def answer(self, nums, k):
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == k:
                return mid
            
            elif nums[mid] > k:
                r = mid - 1
                
            else:
                l = mid + 1
        
result = Solution().answer([1,5,2,3,4,9,7,2,8,5], 9)
print(result)