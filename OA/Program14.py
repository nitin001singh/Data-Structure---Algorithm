# Problem.-> Given an array of size “N”; find the number of triplets; such that A[i] >A[j]< A[k] such that i < j < k ; 

# 1<=N<=1000

# TC : O(N^3)
# SC : O(1)

class Solution:
    def answer(self, nums):
        n = len(nums)
        c = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] > nums[j] < nums[k]:
                        c += 1
                        
        return c
       

result = Solution().answer([8,1,2,3,4,5])
print(result)



# TC : O(N^2 +  N^2 + N)
# SC : O(2N)

class Solution:
    def answer(self, nums):
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        # Build prefix counts
        for j in range(n):
            count = 0
            for i in range(j):
                if nums[i] > nums[j]:
                    count += 1
            pref[j] = count

        # Build suffix counts
        for k in range(n):
            count = 0
            for l in range(k + 1, n):
                if nums[k] > nums[l]:
                    count += 1
            suff[k] = count

        # Calculate total valid quadruplets
        total = 0
        for j in range(n):
            for k in range(j + 1, n):
                if nums[j] < nums[k]:
                    total += pref[j] * suff[k]

        return pref, suff, total


result = Solution().answer([8,1,2,3,4,5])
print(result)



# Follow up :-> Given an array of size “N”; find the number of quadruplets; such that A[i] > A[j] < A[k] >A[l] such that i < j < k < l ; 


class Solution:
    def answer(self, A):
        n = len(A)
        pref = [0] * n
        suff = [0] * n

        # Compute pref[j]: how many i < j such that A[i] > A[j]
        for j in range(n):
            for i in range(j):
                if A[i] > A[j]:
                    pref[j] += 1

        # Compute suff[k]: how many l > k such that A[k] > A[l]
        for k in range(n):
            for l in range(k + 1, n):
                if A[k] > A[l]:
                    suff[k] += 1


        # print(pref, suff)
        # Count valid pairs (j, k)
        count = 0
        for j in range(n):
            for k in range(j + 1, n):
                if A[j] < A[k]:
                    count += pref[j] * suff[k]

        return count


print(Solution().answer([8, 1, 2, 3, 4, 5]))