# Brute Force 

# TC: O((m + n) * log(m + n))
# SC : O(m + n)

# class Solution:
#     def answer(self, arr1, arr2):
#         modified_arr = arr1 + arr2
#         modified_arr.sort()
#         length = len(modified_arr)
        
#         if length % 2 == 1:
#             median = modified_arr[length // 2]
#         else: 
#             median = (modified_arr[length // 2 - 1] + modified_arr[length // 2]) / 2

#         return round(median, 1)
                
# result = Solution().answer([1,2],[3,4])
# print(result)



class Solution:
    def answer(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Handling edges using float('-inf') and float('inf')
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if partition is correct
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

                
result = Solution().answer([1,2],[3,4])
print(result)





2 3 4 8   4 9 100 5 