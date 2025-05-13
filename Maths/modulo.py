class Solution:
    def answer(self, a,b,k):
        result1 = (a % k + b % k) % k
        result2 = (a % k * b % k) % k
        result3 = (a % k - b % k + k) % k
        
        print(result1)
        print(result2)
        print(result3)
        
        
        
result = Solution().answer(6,12,18)