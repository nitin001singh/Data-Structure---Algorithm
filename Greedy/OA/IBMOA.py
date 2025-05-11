
# Given an array of size N; and a target -> find the minimum number of operations needed to make all elements of array equal to target -> there are multiple target in order of Q;


# Brute Force 
# TC : O(N*Q) 
# SC : O(1)

# class Solution : 
#     def answer(self, nums, target):
#         n = int(input("Enter number of array element : "))
#         nums = []
#         for _ in range(n):
#             nums.append( int(input("Enter array element : ")) )
            
#         q = int(input("Enter number of queries : "))
        
#         for _ in range(q):
#             target = int(input("Enter target  : "))
#             operation  = 0
#             for value in nums:
#                 operation += abs(value - target)
                
#             print(operation , end="\n")
        
            
# result = Solution().answer([1 ,2 ,3 ,4, 5], 3 )
# print(result)




# Optimization:-> 


# If target > all numbers in the array ->(target > max element of array)

# -> answer = target*n - sum; =>O(1)

# If target < all numbers in the array ->(target < min element of the array) 

# -> answer = sum - target*n; 


# TC - O(N + NlogN + QlogN)
# SC : O(N)

class Solution:
    def answer(self, nums, target):
        n = int(input("Enter number of array elements: "))
        nums = []
        for _ in range(n):
            nums.append(int(input("Enter array element: ")))

        nums.sort()
        prefix = [0] * (n + 1)
        total_sum = 0

        for i in range(n):
            total_sum += nums[i]
            prefix[i + 1] = prefix[i] + nums[i]
            
            

        q = int(input("Enter number of queries: "))
        for _ in range(q):
            target = int(input("Enter target: "))

            low, high, idx = 0, n - 1, -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1

            
            left_part = target * (idx + 1) - prefix[idx + 1]
            right_part = (total_sum - prefix[idx + 1]) - target * (n - idx - 1)
            print(f"Minimum operations for target {target}: {left_part + right_part}")

# Run the solution
result = Solution().answer([], 0)
