# Brute Force 

# Tc : O(N)
# SC : O(N)

# class Solution:
#     def singleElementInSorted(self, nums):
#         maps = {}
#         for value in nums:
#             if value in maps:
#                 maps[value] += 1
#             else:
#                 maps[value] = 1
                
#         return maps
    
    
# result = Solution().singleElementInSorted([3, 3 ,7 ,7 ,10, 11 ,11])

# for value, freq in result.items():
#     if freq == 1:
#         print(value)


# Optimal
# TC : O(logN)
# SC O(1)


class OpyimizeSolution:
    def singleElementInSorted(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
                
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
                
        return nums[left]
                
            
            
    
    
result = OpyimizeSolution().singleElementInSorted([3, 3 ,7 ,7 ,10, 11 ,11])
print(result)
