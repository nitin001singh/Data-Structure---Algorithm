# TC : O(log2(N))
# SC : O(1)

class Solution:
    def answer(self, nums, k):
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == k:
                return True
            
            elif nums[mid] > k:
                r = mid - 1
                
            else:
                l = mid + 1
                
        return False
        
result = Solution().answer([1,5,2,3,4,9,7,2,8,5], 7)
print(result)