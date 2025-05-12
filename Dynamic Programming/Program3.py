# Select maximum sum subset from the two arrays such that no two elements are consecutive.

class Solution:
    def answer(self, a, b):
        n = len(a)
        dp = [0] * n        
        
        dp[0] = max(a[0], b[0])
        dp[1] = max(dp[0], max(a[1], b[1]))
        
        for i in range(2, n):
            x = dp[i - 1]
            y = b[i] + dp[i - 2]
            z = a[i] + dp[i - 2]
            dp[i] = max(x, y, z)
        
        print("Answer:", dp[n-1])


res = Solution().answer([1,5,3,21234],[-4509 ,200,3,40])