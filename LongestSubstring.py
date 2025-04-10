# TC O(N)
# SC O(N)

# class Solution:
#     def longestSubArray(self, strs):
#         if len(strs) < 1 :
#             return 0
    
#         hashset = set()
#         maxCount = 1
#         left = 0
#         right = 1
#         hashset.add(strs[0])
        
#         while right < len(strs):
#             while strs[right] in hashset:
#                 hashset.remove(strs[left])
#                 left += 1

#             hashset.add(strs[right])
#             right += 1
#             maxCount = max(maxCount, right - left)
        
#         return maxCount
            
             
    
# result = Solution().longestSubArray('pwwkew')
# print(result)


# TC O(N)
# SC O(N)

class Solution:
    def longestSubArray(self, strs):
        if len(strs) < 1 :
            return 0
    
        hashmap = {}
        maxCount = 0
        left = 0
        
        for right, chars in enumerate(strs):
            if chars in hashmap and hashmap[chars] >= left:
                left = hashmap[chars] + 1

            hashmap[chars] = right
            maxCount = max(maxCount, right - left + 1)
        
        return maxCount
            
             
    
result = Solution().longestSubArray('abcabcbbcdef')
print(result)