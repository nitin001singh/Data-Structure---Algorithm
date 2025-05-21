# https://docs.google.com/document/d/1esfWAWutnC-WEOJT0N9vC3Z5EFkUteCrHCtE8rqetEM/edit?tab=t.0

# Tc: O(N)
# SC : O(N)


class Solution:
    def answer(self, nums):
        hashmap = {}
        for val in nums:
            hashmap[val] = hashmap.get(val, 0) + 1
            
        ans = 0
        check = 1
        for x in hashmap:
            if hashmap[x] == 1:
                check = 0
            
            if hashmap[x] % 3 == 0:
                ans += (hashmap[x] // 3)
            else:
                ans += (hashmap[x] // 3) + 1
                
            
        if check == 0:
            return -1
            
        return ans
        
result = Solution().answer([2,4,6,6,4,2,4])
print(result)