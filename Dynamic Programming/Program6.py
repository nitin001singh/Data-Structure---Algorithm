# Find the largest valid substring - Valid string is a string where adjacent pair of char have diff<=k  


class Solution:
    def answer(self, word, k):
        n = len(word)
        dp = [0] * n
        dp[0] = 1
        
        max_len = 1 
        max_index = 0

        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i - 1])) <= k:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
    
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
    
        start_index = max_index - max_len + 1
        print(word[start_index:start_index + max_len])


res = Solution().answer('bbbbb',2) 
# print(res)