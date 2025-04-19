# Brute Force

# TC : O(N)
# SC : O(N)


class Solution:
    def answer(self , nums, k):
        n = len(nums)
        left = 0
        right = k
        resp = []
        while left < right and right <= n:
            maxElem = max(nums[left:right])
            resp.append(maxElem)
            left += 1
            right += 1
        return resp
            
         
result = Solution().answer( [1] , 1 )
print(result)
