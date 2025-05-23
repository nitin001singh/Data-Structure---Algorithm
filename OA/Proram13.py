# TC : O(N^2)
# SC : O(N)

class Solution:
    def answer(self, nums1,nums2, nums3, nums4):
        dictionary = {}
        for n1 in nums1:
            for n2 in nums2:
                numberNeeded = -(n1 + n2)
                dictionary[numberNeeded] = dictionary.get(numberNeeded, 0) + 1
                
        numberOfTuples = 0
        for n3 in nums3:
            for n4 in nums4:
                numberOfTuples += dictionary.get(n3 + n4, 0) 
            
        return numberOfTuples

        
result = Solution().answer([1,2], [-2,-1] , [-1,2], [0,2])
print(result)