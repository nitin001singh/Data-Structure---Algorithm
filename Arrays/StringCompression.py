class Solution:
    def answer(self, charList):
        resp = []
        count = 1
        
        for index in range(1 , len(charList)):
            if charList[index] == charList[index -1]:
                count += 1
            else:
                resp.append(charList[index - 1])
                if count > 1:
                    for freq in str(count):
                        resp.append(freq)
                        
                count = 1
                
        resp.append(charList[-1])        
        
        if count > 1 :
            for freq in str(count):
                resp.append(freq)
                
        for index in range(len(resp)):
            charList[index] = resp[index]
            
            
        return charList[:len(resp)] , len(charList[:len(resp)])
        

result = Solution().answer( ["a","a","b","b","c","c","c"] )
print(result)
