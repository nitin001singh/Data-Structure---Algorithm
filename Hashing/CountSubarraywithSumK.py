# Generate all Subarray

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


class Solution:
    def answer(self, nums, k):
        summ = 0
        count = 0
        prefix_sum_count = {0: 1}

        for num in nums:
            summ += num
            if (summ - k) in prefix_sum_count:
                count += prefix_sum_count[summ - k]
            prefix_sum_count[summ] = prefix_sum_count.get(summ, 0) + 1

        return count


result = Solution().answer([1, 7, 5, 9, 2, 12, 3], 9)
print(result)

