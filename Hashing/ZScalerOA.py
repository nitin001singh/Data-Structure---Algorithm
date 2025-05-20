# Brute Force 

# TC : O(N^2)
# SC : O(N)

# class Solution:
#     def answer(self , nums):
#         step = 0
#         while len(set(nums)) > 1:
#             step_count, nums = self.calculateInput(nums)
#             step += step_count

#         return step
            
    
#     def calculateInput(self , nums):
#         largestValue = float("-inf")
#         slargestValue =  float("-inf")
#         for value in nums:
#             if value > largestValue:
#                 largestValue = value
            
#         for value in nums:
#             if value > slargestValue and value != largestValue :
#                 slargestValue = value
                
            
#         resp = []
#         resp.append(nums.count(largestValue))

#         for index in range(len(nums)):
#             if nums[index] == largestValue:
#                 nums[index] = slargestValue
                
#         resp.append(nums)
                
#         return resp
    
    
# result = Solution().answer([5,2,1])
# print(result)
       
       
       
# optimal 

# TC : O(n + k log k)
# SC : O(k) 

class Solution:
    def answer(self , nums):
        hashmap = {}
        for value in nums:
            hashmap[value] = hashmap.get(value, 0) + 1
            
        sortedMap = sorted(hashmap, reverse=True)     

        step  = 0
        for key in  range(len(sortedMap)-1):
            count = hashmap[sortedMap[key]]
            step += count
            hashmap[sortedMap[key+1]] += step
            hashmap[sortedMap[key]] = 0
            
        return step
            
result = Solution().answer([5,2,1])
print(result)
        
        
        
        
        