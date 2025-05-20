# Count Subarrays with given XOR

# Optimal

# TC : O(N)
# SC : O(N)

class Solution:
    def answer(self, nums, k):
        c = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            c ^= num
            vl= c ^ k
            count += hashmap.get(vl, 0)
            hashmap[c] = hashmap.get(c, 0) + 1

        return count


result = Solution().answer([5, 6, 7, 8, 9], 5)
print(result)

