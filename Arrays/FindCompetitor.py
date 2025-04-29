class Solution:
    def answer(self, scores):
        scores.sort()
        
        print(scores)  

        prev_sum = 0
        curr_index = 0
        group_size = 1
        categories = 0
        n = len(scores)
        while curr_index + group_size <= n:
            # print(curr_index , group_size)
            group_sum = sum(scores[curr_index : curr_index + group_size])
            if group_sum > prev_sum:
                prev_sum = group_sum
                curr_index += group_size
                group_size += 1
                categories += 1
            else:
                break 

        return categories
    
result = Solution().answer([14, 5, 9, 7, 2, 4])
print(result)