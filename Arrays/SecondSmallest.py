class Solution:
    def secondSmallest(self, nums):
        if not nums or len(nums) < 2:
            return -1
        smallest = nums[0]
        ssmallest = -1
        
        for value in nums:
            if value < smallest:
                ssmallest = smallest
                smallest = value
            elif value < ssmallest and value != smallest:
                ssmallest = value
                
        return ssmallest
    
    
    def secondLargest(self, nums):
        if not nums and len(nums) < 2 :
            return -1
        
        
        largest = nums[0]
        slargest = -1
        for value in nums:
            if value > largest:
                slargest = largest
                largest = value
            elif value > slargest and value != largest:
                slargest = value
                
        return slargest
    
    
    
    
    
    
    
    
result = Solution().secondSmallest([12, 35, 1, 10, 34, 1])
result1 = Solution().secondLargest([12, 35, 1, 10, 34, 1])
print(result, result1)