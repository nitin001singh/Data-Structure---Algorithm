# Brute Force

# TC : O(N^2)
# SC : O(N)

# class Solution:
#     def answer(self, word):
#         hashmap = {}
#         for chars in word:
#             if chars in hashmap:
#                 hashmap[chars] += 1
#             else:
#                 hashmap[chars] = 1
                
        
#         print(hashmap)
        
#         for chars , freq in hashmap.items():
#             if freq == 1:
#                 return word.index(chars)
                
#         return -1

# result = Solution().answer('leetcode')
# print(result)

# Better

# TC : O(N)
# SC : O(N)

class Solution:
    def answer(self, word):
        hashmap = {}
        for chars in word:
            if chars in hashmap:
                hashmap[chars] += 1
            else:
                hashmap[chars] = 1
                
        for x in range(len(word)):
            if hashmap[word[x]] == 1:
                return word[x]
        return -1

result = Solution().answer('leetcode')
print(result)