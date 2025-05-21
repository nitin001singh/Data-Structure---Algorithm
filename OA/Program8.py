# Tc : O(N)
# SC : O(N)

class Solution:
    def answer(self, nums, k):
        summ = 0
        length = float("-inf")
        count = 0
        n = len(nums)
        hashmap = {0: -1}

        for i in range(n):
            summ += nums[i]

            if summ - k in hashmap:
                curr_len = i - hashmap[summ - k]
                if curr_len > length:
                    length = curr_len
                    count = 1
                elif curr_len == length:
                    count += 1


            if summ not in hashmap:
                hashmap[summ] = i

        return length, count if length != float("inf") else 0

        
result = Solution().answer( [10,5,2,7,1,9,8,7], 15)
print(result)