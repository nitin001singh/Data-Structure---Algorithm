# "Find the largest valid substring - , Valid string is a string where any pair of characters have diff<=k , A substring is only valid if max char [i……i] and min char [i…..j]  -> max - min <=k "


# TC : O(N)
# SC : O(1)

class Solution:
    def answer(self, s, k):
        maxLength = 0
        left = 0
        hashmap = {}
        for right in range( len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
               hashmap[s[right]]  = 1
            
            
        minChar = min(hashmap.keys())
        maxChar = max(hashmap.keys())
        
        diff = ord(maxChar) - ord(minChar)
        
        while diff > k:
            hashmap[s[left]] -= 1
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1
            
            minChar = min(hashmap.keys())
            maxChar = max(hashmap.keys())
            diff = ord(maxChar) - ord(minChar)
        
        maxLength =  max(maxLength , right - left + 1)

        return maxLength
result = Solution().answer("bbcdg",5)
print(result)