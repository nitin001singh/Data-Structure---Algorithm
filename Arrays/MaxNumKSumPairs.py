# Brute Force 

# TC : O(N^3)
# SC : O(1)

# class Solution:
#     def answer(self , nums, target):
#         n = len(nums)
#         length = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 # print(nums[i], nums[j])
#                 s = 0
#                 for k in range(i, j+1):
#                     s+= nums[k]
                
#                 if s == target:
#                     length = max(length, j - i + 1)
                    
                    
#         return length
    
    
# result = Solution().answer([1,2,3,4], 6)
# print(result)


# Brute Force 

# TC : O(N^2)
# SC : O(1)


# class Solution:
#     def answer(self , nums, target):
#         n = len(nums)
#         length = 0
#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s+= nums[j]
#                 if s == target:
#                     length = max(length, j - i + 1)
                    
                    
#         return length
    
    
# result = Solution().answer([1,2,3,4], 6)
# print(result)


# Optimal

# TC : O(NlogN)
# SC : O(1)


class Solution:
    def answer(self , nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        maxCount = 0
        while left < right:
            if nums[left] + nums[right] == target:
                maxCount += 1
                right -= 1
                left += 1 
            elif nums[left] + nums[right] > target:
                right -= 1
            else :
                left += 1
        
        return maxCount
                
            
result = Solution().answer([5,4,1,2,3], 5)
print(result)
