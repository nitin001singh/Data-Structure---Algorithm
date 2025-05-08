# Tc : O(n+q)
# Sc : O(n+q)


class Solution :
    def answer(self):
        n = int(input("Enter the number of total values : "))
        arr = []
        for i in range(n):
            arr.append(input("Enter the value for {} index : ".format(i)))
            
        q = int(input("Enter the number of total queries : "))
        
        query = []
        for j in range(q):
            query.append((input("Enter the query {} with comma separated: ".format(j+1))))
            
        
        prefixSum = [0] * len(arr)
        prefixSum[0] = int(arr[0])
        for z in range(1, len(arr)):
            prefixSum[z] = prefixSum[z-1] + int(arr[z])
        
        
        finalOpt= []
        for q in query:
            res = self.getAnswer(prefixSum, q.split(','))
            finalOpt.append(res)
        
        
        return finalOpt
    
    
    def getAnswer(self, prefixSum, query):
        if (int(query[0]) - 1) >= 0:
            return prefixSum[ int(query[1]) ] - (prefixSum[ int(query[0]) - 1 ]  )
        else:
            return prefixSum[ int(query[1]) ]
            

res = Solution().answer()
for x in res:
    print(x, end="\n")