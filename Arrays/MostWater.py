# Brute Force
# TC : O(N2)
# SC : O(1)

# class Solution(object):
#     def maxArea(self, height):
#         maximum = 0
#         for outer in range(0, len(height)):
#             for inner in range(outer +1, len(height)):
#                 area = (inner - outer) * min( height[outer], height[inner] )
#                 maximum = max(area, maximum)
                
#         return maximum
            



# s = Solution()
# result = s.maxArea([1,8,6,2,5,4,8,3,7])
# print(result)


# Optimize 

# TC : O(N)
# SC : O(1)



class OptimizeSolution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxVal = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxVal = max(area, maxVal)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxVal          
            

s = OptimizeSolution()
result = s.maxArea([1,8,6,2,5,4,8,3,7])
print(result)