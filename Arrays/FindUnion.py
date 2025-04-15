# TC : O(m+n)
# SC : O(m+n)

# class Solution:
#     def answer(self, nums1, nums2):
#         return set(nums1 + nums2)
        
        
# result = Solution().answer( [1,2,3,4,5,6,7] , [2,3,4,4,5] )  
# print(result)   


# TC : O(m+n)
# SC : O(m+n)


# class Solution:
#     def answer(self, nums1, nums2):
#         hashmap = {}
#         for index, value in  enumerate(nums1):
#             if value in hashmap:
#                 hashmap[value] += 1
#             else:
#                 hashmap[value] = index
                
#         for index, value in  enumerate(nums2):
#             if value in hashmap:
#                 hashmap[value] += 1
#             else:
#                 hashmap[value] = index   
        
#         return list(hashmap.keys())
    
    
# result = Solution().answer( [1,2,3,4,5,6,7] , [2,3,4,4,5] )  
# print(result)   



# TC : O(m+n)
# SC : O(m+n)


class Solution:
    def answer(self, nums1, nums2):
        hashset = set()
        for index, value in  enumerate(nums1):
            hashset.add(value)
                
        for index, value in  enumerate(nums2):
            hashset.add(value)
        
        return list(hashset)
    
    
result = Solution().answer( [1,2,3,4,5,6,7] , [2,3,4,4,5] )  
print(result)   
