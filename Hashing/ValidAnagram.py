# Brute Force 
# TC :O(NlogN)
# SC: O(1)


# class Solution:
#     def answer(self, s,t):
#         s = "".join(sorted(s))
#         t = "".join(sorted(t))

#         return s == t
        
# result = Solution().answer("abba","abba")
# print(result)


# Optimal
# TC : O(N)
# SC :O(N)

class Solution:
    def answer(self, s,t):
        
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for x in s:
            hashmap[x] = hashmap.get(x,0) + 1
            
        for y in t:
            if y in hashmap:
                hashmap[y] -= 1
            
        for freq in hashmap.values():
            if freq > 0:
                return False
            
        return True
        
result = Solution().answer("abba","abba")
print(result)