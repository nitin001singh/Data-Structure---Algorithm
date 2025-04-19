# Optimal 
# TC : O(S)  s is the total number of characters
# Sc O(1)

# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""

#         for i in range(len(strs[0])):
#             char = strs[0][i]
#             for s in strs[1:]:
#                 if i > len(s) or s[i] != char:
#                     return strs[0][:i]
                
#         return strs[0]
            
        
# result = Solution().longestCommonPrefix( ["flower","flow","flight"] )  
# print(result)   


class Solution:
    def answer(self , strs):
        if not strs:
            return ""
        
        strs.sort()
        n = len(strs)
        
        first = strs[0]
        second = strs[n-1]
        
        left = 0
        while left < len(first):
            if first[left] == second[left]:
                left += 1
            else:
                break
        return first[:left]  if left > 0 else ""
         
result = Solution().answer( ["flower","",""] )
print(result)
