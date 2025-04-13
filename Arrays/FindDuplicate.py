# Floyd Algorithm
# TC : O(N)
# SC : O(1)


class Solution:
    def answer(self, nums):
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast :
                break

        
        ptr1 = slow
        ptr2 = 0

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr2
    
result = Solution().answer([1,2,2,3,4])
print(result)