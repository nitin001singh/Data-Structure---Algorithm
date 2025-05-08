# TC :O(N)
# SC :O(N)

class Solution:
    def answer(self, nums, target):
        hashmap = {}
        count = 0
        for num in nums:
            complement = target - num
            if complement in hashmap:
                count += hashmap[complement]
            hashmap[num] = hashmap.get(num, 0) + 1 
        return count
          
result = Solution().answer([5 ,6 ,5 ,7 ,7, 8], 13)
print(result)




# count = 4

# 13  - 5 = 8
# 13 - 6 = 7
# 13 - 5 = 8
# 13 - 7 = 6
# 13 - 7 = 6

# 13 - 8 = 5




# 8 : 1
# 7 : 2
# 6 : 1
# 5 : 2