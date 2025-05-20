class Solution:
    def smallestIndex(self, nums):
        n = len(nums)
        for index in range(n):
            sum_of_digit = self.sumOfDigit(nums[index])
            # print(sum_of_digit)
            if sum_of_digit == index:
                return index

        return -1
        
    def sumOfDigit(self, nums):
        summ = 0
        while nums > 0:
           summ += nums % 10
           nums //= 10
           
        return summ


      
result = Solution().smallestIndex([1,10,11])
print(result)