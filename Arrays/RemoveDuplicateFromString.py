# Brute force 

# TC : O(N2)
# SC : O(N)


# class Solution:
#     def remove_dupli(self, strs):
#         left = 0
#         right = 1
#         resStr = ""
#         for index in range(len(strs) - 1):
#             if not strs[index] in resStr:
#                 resStr += strs[index]
            
#         return resStr
            
# result = Solution().remove_dupli("abbbcccdefg")
# print(result)


# Optimal Solution 
# TC : O(N)
# SC O(N)

class OptimizeSolution:
    def remove_dupli(self, strs):   
        hashset = set()  
        output =  []
        for index in range(len(strs)):
            if strs[index] not in hashset:
                hashset.add(strs[index])
                output.append(strs[index])
            
        return "".join(output)

result = OptimizeSolution().remove_dupli("abbbcccdefg")
print(result)