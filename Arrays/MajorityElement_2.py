# Brute Force 
# TC : O(n)
# SC : O(n)

# class Solution:
#     def answer(self, nums):
#         hashmap = {}
#         n = len(nums)
#         for value in nums:
#             if value in hashmap:
#                 hashmap[value] += 1
#             else:
#                 hashmap[value] = 1
                

#         flipping = []
#         for value, freq in hashmap.items():
#             if freq > n // 3:
#                 flipping.append(value)

#         return flipping    
    
# result = Solution().answer([3,2,3])
# print(result)




class Solution:
    def answer(self, nums):
        if not nums:
            return []

        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result
 
    
result = Solution().answer([3,2,3,4,4])
print(result)