# counts the number of subarrays in nums that contain at most K distinct integers.

# Tc : O(N^2)
# Tc : O(1)

# class Solution:
#     def answer(self, nums, k):
#         count = 0
#         for j in range(len(nums)):
#             hashmap = {}
#             for z in range(j, len(nums)):
#                 hashmap[nums[z]] = hashmap.get(nums[z], 0) + 1
#                 n = len(hashmap)
#                 if n <= k:
#                     count += 1
                    
#         return count
            

# result = Solution().answer([1 ,2 ,3 ], 2)
# print(result)


# Tc : O(N)
# Tc : O(K)


class Solution:
    def answer(self, nums, k):
        count = 0
        left = 0
        hashmap = {}
        for right in range(len(nums)):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            n = len(hashmap)
            while n > k:
                hashmap[nums[right]] -= 1
                if hashmap[nums[right]] == 0:
                    del hashmap[nums[right]]
                    
                left += 1
                n = len(hashmap)            
            count += right - left + 1
        
        return count
            
result = Solution().answer([1 ,2 ,3 ], 2)
print(result)