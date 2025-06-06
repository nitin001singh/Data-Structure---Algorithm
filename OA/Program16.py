# Find the number of ways to divide the given array in two equal parts. 


class Solution:
    def answer(self, nums):
        tot = sum(nums)
        c= 0
        lhs = 0
        for x in range(len(nums)):
            lhs += nums[x]
            
            rhs = tot - lhs
            
            if lhs == rhs:
                c += 1
                
        return  c 
        
result = Solution().answer([1,1,0,0,1,1])
print(result)


# Find the number of ways to divide the given array in three equal parts. 


class Solution:
    def answer(self, nums):
        total = sum(nums)
        if total % 3 != 0:
            return 0
        
        one_third = total // 3
        two_third = 2 * one_third
        
        count_one_third = 0
        count = 0
        prefix_sum = 0
        

        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            
            if prefix_sum == two_third:
                count += count_one_third 
            
            if prefix_sum == one_third:
                count_one_third += 1
                
        return count

result = Solution().answer([1, 2, 3, 0, 3])
print(result) 


# Find the number of ways to divide the given array in four equal parts. 


class Solution:
    def countWaysToSplitIntoFourParts(self, nums):
        total = sum(nums)
        if total % 4 != 0:
            return 0
        
        part = total // 4
        prefix_sum = 0
        count_part1 = 0
        count_part2 = 0
        count = 0
        
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            
            if prefix_sum == 3 * part:
                count += count_part2
            
            if prefix_sum == 2 * part:
                count_part2 += count_part1

            if prefix_sum == part:
                count_part1 += 1
        
        return count

result = Solution().countWaysToSplitIntoFourParts([1, 1, 1, 1, 1, 1, 1])
print(result) 
