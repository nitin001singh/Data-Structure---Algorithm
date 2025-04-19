class Solution:
    def answer(self , s1, s2):
        
        
        left = 0
        while left < len(s1):
            if s1[left] in s2:
                left += 1
       
        return len(s1) == left
        
         
result = Solution().answer( 'ab', 'eidboaoo' )
print(result)
