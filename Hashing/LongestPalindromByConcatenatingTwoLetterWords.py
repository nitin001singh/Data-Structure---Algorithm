# TC : O(N)
# SC : O(N)

class Solution:
    def answer(self, words):
        ans = 0
        hashmap = {}
        for index in range(len(words)):
            word = words[index]
            revWord = word[::-1]
            
            if revWord in hashmap:
                ans += 4
                hashmap[revWord] -= 1
                if hashmap[revWord] == 0:
                    del hashmap[revWord] 
                
            else:
                hashmap[word] = hashmap.get(word, 0) + 1
            
        
        # print(ans , hashmap)
        
        for word in hashmap.keys():
            if word[0] == word[1]:
                ans += 2
                break
        
        return ans


result = Solution().answer(["ab","ty","yt","lc","cl","ab"])
print(result)