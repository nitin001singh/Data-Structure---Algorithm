# We are given an array of integers(a[n]) . We are given multiple queries of the form : (1, i) which means we need to output the sum of all numbers from index- ‘1’ to index ‘i’ of the array.

class Solution:
    def answer(self, a, w):
        n = len(a)
        dp = [0] * (n + 1)
        i = 0
        while i <= n - 1:
            if i == 0:
                dp[i] = a[i]
            else:
                dp[i] = a[i] + dp[i - 1]
            i += 1
            
        q = 4 
        i = 0
        while i <= q - 1:
            query = w[i]
            print(dp[query]) 
            i += 1
        


res = Solution().answer([6, 7, 3, 2, 2],  [0, 3, 4, 2] )
print(res)
