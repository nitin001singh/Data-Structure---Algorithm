# Given a sorted array of size “N”; find the index of the number in the array which is just greater than x and as close as possible to x.

# -> Upper Bound (x) = Returns index of the number which is just greater than x and as close as possible to x.




# TC : O(N)
# SC : O(1)


class Solution:
    def answer(self, nums, target):
        closest = nums[0]
        min_diff = abs(nums[0] - target)
        
        for num in nums:
            diff = abs(num - target)
            if diff < min_diff:
                min_diff = diff
                closest = num
                
        return closest
                            
result = Solution().answer([1, 3, 5, 7, 9, 11], 6)
print(result)




# TC : O(logN)
# SC : O(1)


class Solution:
    def answer(self, nums, x):
        l = 0
        r = len(nums) - 1
        opt = -1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] > x:
                opt = mid 
                r = mid - 1 
            else:
                l = mid + 1
        
        return opt 
                            
                
    
    
result = Solution().answer([1, 3, 5, 6, 6, 7, 7, 9], 6)
print(result)