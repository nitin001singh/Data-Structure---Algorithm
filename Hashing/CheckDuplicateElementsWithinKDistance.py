# Brute Force 

# TC : O(N * K)
# SC : O(1)
 
# def check_duplicates_within_k(arr, k):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, min(i + k + 1, n)):
#             if arr[i] == arr[j]:
#                 return True
#     return False

# arr = [10, 5, 3, 4, 3, 5, 6]
# k = 3
# if check_duplicates_within_k(arr, k):
#     print("Yes")
# else:
#     print("No")



# TC : O(N)
# SC : O(N)

class Solution :
    def answer(self, arr1,k):
        hashmap = {}
        n = len(arr1)
        for index in range(n):
            if arr1[index] in hashmap:
                difference = index - hashmap[arr1[index]]
                if difference <= k:
                    return True
                hashmap[arr1[index] ] =  index
            else:
                hashmap[arr1[index] ] = index

        return False
        

res = Solution().answer([1,2,3,1],3)
print(res)