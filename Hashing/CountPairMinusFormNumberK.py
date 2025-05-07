# Brute Force 
# TC : O(N^2)
# SC : O(1)

# class Solution:
#     def answer(self, nums, k):
#         n = len(nums)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 diff = abs(nums[i] - nums[j])
#                 if diff == k:
#                     count += 1
                    
#         return count
        
        
        
# result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 2)
# print(result)



# Optimize 
# TC : O(N)
# SC : O(N)



class Solution:
    def answer(self, nums, k):
        count = 0
        hashmap = {}
    
        for num in nums:
            target_minus = num - k
            target_plus = num + k
            if target_minus in hashmap:
                count += hashmap[target_minus]
                
            if k != 0 and target_plus in hashmap: 
                count += hashmap[target_plus]
    
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
    
        return count
        
                
result = Solution().answer([3,1,4,1,5], 2)
print(result)