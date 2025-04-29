# Brute Force 
# Tc : O(N^2)
# Sc : O(N)

# class Solution:
#     def answer(self , temperature):
#         n = len(temperature)
#         ans = [0] * n

#         for i in range(len(temperature)):
#             for j in range(i+1, len(temperature)):
#                 print(temperature[i] ,  temperature[j])
#                 if temperature[j] > temperature[i]:
#                     ans[i] = j-i
#                     break
                
#         return ans
        
         
# result = Solution().answer( [30,40,50,60] )
# print(result)



# Optimal
# Tc : O(N)
# Sc : O(N)

class Solution:
    def answer(self , temperature):
        n = len(temperature)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperature[i] > temperature[stack[-1]]:
                prevIndex = stack.pop()
                ans[prevIndex] = i - prevIndex
            stack.append(i)
                
        return ans
        
         
result = Solution().answer( [30,40,50,60] )
print(result)
