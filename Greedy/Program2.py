# TC : O(NlogN)
# SC : O(1)

class Solution:
    def answer(self, num1, num2):
        num1.sort()
        num2.sort()
        
        mul = 0
        for i in range(len(num1)):
            mul += (num1[i] * num2[i])
            
        return mul
    
result = Solution().answer([1, 3, -5], [-2, 4, 1])
print(result) 
