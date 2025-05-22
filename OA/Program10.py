# > You are given an array of size “N” and two integers “x” and “y” 
# -> Array only consists of integers “x” and “y”
# -> Find the count of subarrays which have equal number of “x” and “y” 


# Brute Force 
# TC : O(N^2)
# SC : O(1)


class Solution:
    def answer(self, nums, a,b):
        c = 0
        n = len(nums)
        for x in range(n):
            ca = 0
            cb = 0
            for y in range(x, n):
                if nums[y] == a:
                    ca += 1
                    
                if nums[y] == b:
                    cb += 1
                    
                if ca == cb:
                    c += 1
                    
        return c
            
result = Solution().answer( [1, 2, 1, 1, 2], 1,2)
print(result)


# Optimization
# TC : O(N)
# SC : O(N)


class Solution:
    def answer(self, nums, a,b):
        count = 0
        prefix_sum = 0
        sum_freq = {0: 1}

        for val in nums:
            if val == a:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            count += sum_freq.get(prefix_sum, 0)
            sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
                    
        return count
            
result = Solution().answer( [1, 2, 1, 1, 2], 1,2)
print(result)



# Follow up :-  -> You are given an array of size “N” and 5 distinct integers “x” “y” “z” “w” “b”
# -> Array only consists of integers “x” “y” “z” “w” “b”
# -> Find the count of subarrays which have equal number of “x”  “y” “z” “w” “b” 


#  Solution :- Let's solve the easiest version we solved before again :-> 

# -> c2[j] - c2[i-1] = c1[j] - c1[i-1] 

# ->      c2[i-1] - c1[i-1]  = c2[j] - c1[j]


# Easy Version for 2 number

class Solution:
    def answer(self, nums, a,b):
        c = 0
        hashmap = {0: 1}
        n = len(nums)
        ca = 0
        cb = 0
        for y in range(n):
            if nums[y] == a:
                ca += 1
                
            if nums[y] == b:
                cb += 1
                
            d = cb - ca
            c += hashmap.get(d, 0)
            hashmap[d] = hashmap.get(d, 0) + 1
                    
        return c
            
result = Solution().answer( [1, 2, 1, 1, 2], 1,2)
print(result)



# Easy Version for 3 number


class Solution:
    def answer(self, nums, a,b,c):
        count = 0
        hashmap = {0: 1}
        n = len(nums)
        ca = 0
        cb = 0
        cc = 0
        for y in range(n):
            if nums[y] == a:
                ca += 1
                
            elif nums[y] == b:
                cb += 1
                
            elif nums[y] == c:
                cc += 1
                
            d1 = cb - ca
            d2 = cc - cb

            count += hashmap.get((d1,d2), 0)
            hashmap[(d1,d2)] = hashmap.get((d1,d2), 0) + 1
                    
        return count
            
result = Solution().answer( [1, 2, 3, 1, 1, 2,3,3], 1,2,3)
print(result)



# Easy Version for 5 number



class Solution:
    def answer(self, nums, a,b,c,d,e):
        count = 0
        hashmap = {0: 1}
        n = len(nums)
        ca = 0
        cb = 0
        cc = 0
        cd = 0
        ce = 0
        for y in range(n):
            if nums[y] == a:
                ca += 1
                
            elif nums[y] == b:
                cb += 1
                
            elif nums[y] == c:
                cc += 1
            elif nums[y] == d:
                cd += 1
            elif nums[y] == e:
                ce += 1
                
            d1 = cb - ca
            d2 = cc - cb
            d3 = cd - cc
            d4 = ce - cd

            count += hashmap.get((d1,d2,d3,d4), 0)
            hashmap[(d1,d2,d3,d4)] = hashmap.get((d1,d2,d3,d4), 0) + 1
                    
        return count
            
result = Solution().answer( [1, 2, 3, 1, 1, 2,3,3,4,4,5,5], 1,2,3,4,5)
print(result)