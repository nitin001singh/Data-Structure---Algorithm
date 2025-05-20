# 2657. Find the Prefix Common Array of Two Arrays

# TC: O(N^2)
# SC: O(N)
class Solution:
    def answer(self, nums1, nums2):
        n = len(nums1)
        result = []
        for i in range(n):
            prefixA = set(nums1[:i+1])
            prefixB = set(nums2[:i+1])
            common = prefixA.intersection(prefixB)
            result.append(len(common))
        return result
            


result = Solution().answer([1,3,2,4], [3,1,2,4])
print(result)



# Optimal

# TC: O(N)
# SC: O(N)

class Solution:
    def answer(self, nums1, nums2):
        n = len(nums1)
        seenA = set()
        seenB = set()
        commonSeen = set()
        count = 0
        result = []
        
        for i in range(n):
            seenA.add(nums1[i])
            seenB.add(nums2[i])
            
            if nums1[i] in seenB and nums1[i] not in commonSeen:
                count += 1
                commonSeen.add(nums1[i])
            
            if nums2[i] in seenA and nums2[i] not in commonSeen:
                count += 1
                commonSeen.add(nums2[i])
            result.append(count)
            
        return result

result = Solution().answer([1,3,2,4], [3,1,2,4])
print(result)
