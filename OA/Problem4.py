# https://www.desiqna.in/13650/google-girl-hackathon-coding-questions-solutions-2023-kumar

# 1 ≤ a[i] ≤ 100000
# 1 ≤ k ≤ 100000
# So, a[i] - k ≥ 1 and a[i] + k ≤ 100000


# Tc: O(N)
# SC : O(1)


class Solution:
    def answer(self, nums, k):
        size = 100002 
        b = [0] * size

        for x in nums:
            l = x - k 
            r = x + k
            b[l] += 1
            b[r + 1] -= 1

        maxi = 0
        for i in range(1, size):
            b[i] += b[i - 1]
            maxi = max(maxi, b[i])

        return maxi
            
  
        
result = Solution().answer([5,8,10],3)
print(result)