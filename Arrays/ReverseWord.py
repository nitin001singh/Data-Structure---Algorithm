# TC: O(N)
# SC: O(N)

class Solution:
    def answer(self , str):
        return " ".join(str.strip().split()[::-1])
    
result = Solution().answer('a good   example')
print(result)


