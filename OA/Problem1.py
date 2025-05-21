# https://leetcode.com/discuss/post/3114099/amazon-oa-intern-2024-by-anonymous_user-57od/

class Solution:
    def answer(self, s,t):
        hashmap1 = {}
        for val in s:
            hashmap1[val] = hashmap1.get(val, 0) + 1
            
        hashmap2 = {}
        for val in t:
            hashmap2[val] = hashmap2.get(val, 0) + 1
            
              
        count = float("inf")
        for x in t:
            if x not in hashmap1:
                return 0
            
            val = hashmap1[x] // hashmap2[x]
            count = min(count, val)
       
        return count
        
result = Solution().answer('mononmmo','mon')
print(result)