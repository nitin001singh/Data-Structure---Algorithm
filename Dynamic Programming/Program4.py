# Frog - 1 

class Solution:
    def answer(self, a):
        n = len(a)
        dp = [0] * n

        dp[0] = 0
        dp[1] = abs(a[0] - a[1])

        for i in range(2, n ):
            dp[i] = min(   dp[i-1] + abs(a[i] - a[i-1])   ,    dp[i-2] + abs(a[i] - a[i-2])   )

        return dp[-1]


res = Solution().answer([10 ,30, 40, 20]) 
print(res)