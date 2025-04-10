# Brute Force 
# TC: O(n! * (n + log(n!))) → exponential
# SC : O(n * n!)

# import itertools
# class Solution:
#     def nextGreaterElement(self, num):
#         num = str(num)
#         if not num:
#             return -1 
#         if len(num) < 3:
#             return num[::-1]
        
#         permutations = ["".join(value) for value in itertools.permutations(num) ]
#         permutations_list = sorted(list(map(int, permutations)))
#         return [ val for val in permutations_list if val > int(num)][0]
        

# result = Solution().nextGreaterElement(8516)
# print(result)


# Optimize
# TC : O(d)
# SC : O(d)

class Solution:
    def nextGreaterElement(self, nums):
        numList = list(str(nums))
        length = len(numList)
        
        i = self.getFirstDecreasingNumber(numList)
        if i == -1:
            return i
        
        j = self.getNextLargerDigitRight(numList, i)
        
        print(i,j)

        numList[i] , numList[j] = numList[j], numList[i]
        numList[i+1:] = numList[i+1:][::-1]
        
        result = int(''.join(numList))
        return result if result <= 2**31 - 1 else -1


    def getFirstDecreasingNumber(self, numList):
        for i in range(len(numList) - 2, -1, -1):
            if numList[i] < numList[i + 1]:
                return i
        return -1
                
    def getNextLargerDigitRight(self, numList, i):
        for index in range(len(numList) - 1, i, -1):
            if numList[index] > numList[i]:
                return index
        return -1
        
result = Solution().nextGreaterElement(84652543)
print(result)
