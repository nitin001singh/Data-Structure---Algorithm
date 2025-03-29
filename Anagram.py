# We can optimize it more 

# TC : O(N)
# SC : O(N)

# class Solution:
#     def anagram(self, strs):
#         maps = {}
#         for value in strs:
#             hashKey = self.getHashKey(value)
#             if hashKey in maps:
#                 maps[hashKey].append(value)
#             else:
#                 maps[hashKey] = [value]
                
#         return maps.values()
                
#     def getHashKey(self, word):
#         asciiList = [0] * 26 
#         for character in word:
#             index = ord(character) - 97
#             asciiList[index]  += 1
            
#         return tuple(asciiList)
    
    
# result = Solution().anagram(["eat","tea","tan","ate","nat","bat"])
# print(result)



# This is more optimized because we are not using any extra checkes dueto defualtdict
# TC : O(N)
# SC : O(N)


from collections import defaultdict

class OptimizeSolution:
    def anagram(self, strs):
        maps = defaultdict(list)
        for value in strs:
            hashKey = self.getHashKey(value)
            maps[hashKey].append(value)
                
        return list(maps.values())
                
    def getHashKey(self, word):
        asciiList = [0] * 26 
        for character in word:
            index = ord(character) - 97
            asciiList[index]  += 1
            
        return tuple(asciiList)
    
    
result = OptimizeSolution().anagram(["eat","tea","tan","ate","nat","bat"])
print(result)