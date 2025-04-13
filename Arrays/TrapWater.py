# Brute Force 
# TC : O(N2)
# SC : O(1)

# class Solution:
#     def trap(self, height):
#         if not height:
#             return 0
#         waterCount = 0
#         for index, value in enumerate(height):
#             biggestLeft = self.getbiggestLeft(height, index)
#             biggestRight = self.getbiggestRight(height, index)
            
#             # print( value , ' => ', biggestLeft ," : ", biggestRight)
            
#             if biggestLeft > value and biggestRight > value:
#                 waterCount += min(biggestLeft, biggestRight)  - value
                
#         return waterCount

#     def getbiggestLeft(self, height, index):
#         maxVal = 0
#         for i in range(0, index):
#             if height[i] > maxVal:
#                 maxVal = height[i]
                
#         return maxVal
    
#     def getbiggestRight(self, height, index):
#         maxVal = 0
#         for i in range(index+1, len(height)):
#             if height[i] > maxVal:
#                 maxVal = height[i]
#         return maxVal
       
    
# res = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
# print(res)




# Optimize 
# TC : O(N)
# SC : O(N)


# class Practise:
#     def resp (self, nums):
#         if not nums:
#             return 0
        
#         n = len(nums)
#         biggestLeft = [1] * n
#         biggestRight = [1] * n
        
#         maxL = 0
#         maxR = 0
#         waterCount = 0
        
#         for index in range(n):
#             biggestLeft[index] = maxL
#             maxL = max(biggestLeft[index], nums[index])
            
#             rightIndex = n - index - 1
#             biggestRight[rightIndex] = maxR
#             maxR = max(biggestRight[rightIndex], nums[rightIndex] )
            
#         # print(biggestLeft, biggestRight)
        
#         for index in range(len(nums)):
#             minLevel = min(biggestLeft[index], biggestRight[index]) 
#             if minLevel > nums[index]:
#                 waterCount += min(biggestLeft[index], biggestRight[index]) - nums[index]
            
#         return waterCount
                
            
            

    
# result = Practise().resp([0,1,0,2,1,0,1,3,2,1,2,1])
# print(result)

class OptimizeSolution:
    def trap(self, height):
        if not height:
            return 0

        n = len(height)
        left = [0] * n
        right = [0] * n
        temp = 0
        temp1 = 0
        for index in range(n):
            left[index] = temp
            temp = max(temp, height[index]) 
            
        
        for index in range(n-1, -1, -1):
            right[index] = temp1
            temp1 = max(temp1, height[index])
            
        waterCount= 0
        for index in range(n):
            waterCount += max(0,(min(left[index], right[index]) - height[index]))
        
        return waterCount
    

    
res = OptimizeSolution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)


