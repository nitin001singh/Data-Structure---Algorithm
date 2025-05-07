# # Generate all Subarray

# def generate_all_subarrays(nums):
#     n = len(nums)
#     subarrays = []
#     for i in range(n): 
#         for j in range(i, n): 
#             subarrays.append(nums[i:j+1])  
#     return subarrays

# nums = [1, 7, 5, 9]
# all_subarrays = generate_all_subarrays(nums)
# print(all_subarrays)



# Brute Force 
# Tc : O(N^2)
# SC : O(1)

class Solution:
    def answer(self, nums,k):
        n = len(nums)
        count = 0
        for i in range(n):
            currentSum = 0
            for j in range(i, n):
                currentSum += nums[j]
                if currentSum == k:
                    count += 1

        return count
    
result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 9)
print(result)


# Optimal

# TC : O(N)
# SC : O(N)

class Solution:
    def answer(self, nums, k):
        cumSum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            cumSum += num
            if (cumSum - k) in hashmap:
                count += hashmap[cumSum - k]
            hashmap[cumSum] = hashmap.get(cumSum, 0) + 1

        return count


result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 9)
print(result)

