# Optimal 
# TC : O(S)  s is the total number of characters
# Sc O(1)

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i > len(s) or s[i] != char:
                    return strs[0][:i]
                
        return strs[0]
            
        
result = Solution().longestCommonPrefix( ["flower","flow","flight"] )  
print(result)   
