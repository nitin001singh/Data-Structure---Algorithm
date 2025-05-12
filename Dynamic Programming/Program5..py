# Frog - 2

# TC :- O(N * K)
# SC :- O(N) (dp[n]) 

class Solution:
    def answer(self, a, k):
        n = len(a)
        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(a[0] - a[1])

        i = 2
        while i < n:
            answer = float('inf')
            j = 1
            while j <= k and i - j >= 1:
                yy = dp[i - j] + abs(a[i] - a[i - j])
                answer = min(answer, yy)
                j += 1
            dp[i] = answer
            i += 1

        print(dp[-1])


res = Solution().answer([10 ,20,10], 2) 
print(res)