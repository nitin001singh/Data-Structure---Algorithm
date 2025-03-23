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
        for index in range(len(height)):
            waterCount += max(0,(min(left[index], right[index]) - height[index]))
        
        return waterCount
    

    
res = OptimizeSolution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)


