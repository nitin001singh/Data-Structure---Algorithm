# "Given an array of integers(positive as well as negative) ,select some elements from this array(select a subset) such that:-
# 1. Sum of those elements is maximum(Sum of the subset is maximum) .
# 2. No two elements in the subset should be consecutive."


class Solution:
    def answer(self, a):
        n = len(a)
        dp = [0] * n
        l = 0
        dp[0] = max(a[0], l)
        dp[1] = max(a[1], max(a[0], l))
        # we calculate the formula dp[i] = max(dp[i-1], a[i] + dp[i-2])
        i = 2
        while i < n:
            dp[i] = max(dp[i - 1], a[i] + dp[i - 2])
            i += 1
        
        print(dp[n-1])
        


res = Solution().answer([2,4,6,7,8])
print(res)
