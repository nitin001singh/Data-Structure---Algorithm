# Brute Force

# TC : O((m+n) * log(m+n))
# SC : O(m+n)


class Solution:
    def mergeSortedArray(self, nums1, m , nums2 , n):
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1 
            
result = Solution().mergeSortedArray([1,2,3,0,0,0] , 3 , [2,5,6] , 3 )
print(result)