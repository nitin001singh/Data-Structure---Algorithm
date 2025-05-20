# 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it. Return the number of nice sub-arrays.


# Brute Force 
# TC: O(N^3)
# SC : O(N)
class Solution:
    def answer(self, nums, k):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i, n):
                oddCount =  len([1 for _ in nums[i:j+1] if _ % 2 != 0])
                if oddCount==k:
                    count += 1
        return count

result = Solution().answer([2,2,2,1,2,2,1,2,2,2], 2)
print(result)



# Optimal
# TC: O(N)
# SC : O(N)


class Solution:
    def answer(self, nums, k):
        n = len(nums)
        count = 0
        currSum = 0
        hashmap = {} 
        
        for i in range(n):
            nums[i] = 0 if nums[i] % 2 == 0 else 1
            
        for i in range(n):
            currSum += nums[i]
            
            if currSum == k:
                count += 1

            if currSum - k in hashmap:
                count += hashmap[currSum - k]
                
            hashmap[currSum] = hashmap.get(currSum, 0) + 1
            

        return count

result = Solution().answer([1,1,2,1,1], 3)
print(result)