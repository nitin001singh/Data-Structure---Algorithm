# TC: O(N)
# SC: O(1)

class Solution:
    def answer(self , s, t):
        left = 0
        right = 0
        
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
                
        return left == len(s)
    
result = Solution().answer('aaaaaa','bbaaaa')
print(result)


