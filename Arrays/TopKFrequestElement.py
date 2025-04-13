class Solution:
    def answer(self, nums, k):
        hashmap = {}
        for index in range(len(nums)):
            if nums[index] in hashmap:
                hashmap[nums[index]] += 1
            else:
                hashmap[nums[index]] = 1
                

        flippedList = [ [] for _ in range(len(nums) + 1) ]
        for key, value in hashmap.items():
            flippedList[value].append(key)
            
        
        # print(hashmap, flippedList)
            
        opt = []
        for index in range(len(flippedList)-1,-1, -1):
            for freq in flippedList[index]:
                opt.append(freq)
                if len(opt) == k:
                    return opt
                
            
        return opt
        

result = Solution().answer( [1,1,1,2,2,3], 2) 
print(result)   
