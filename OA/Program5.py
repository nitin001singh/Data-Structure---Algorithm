# Tc: O(m + n)    => n = len(nums) ,m = len(points)
# SC : O(N)


class Solution:
    def answer(self, lamps, points):
        b = []
        for lamp in lamps:
            b.extend(lamp)
            
            
        lamp = [0] * (max(b) + 5)
        
        for inputval in lamps:
            l , r = inputval
            lamp[l] += 1
            lamp[r+1] -= 1

        for x in range(1, len(lamp)):
            lamp[x] = lamp[x-1] + lamp[x]


        for p in points:
            print(lamp[p], end=" ")


result = Solution().answer( [[1,7],[5,11],[7,9]], [7,1,5,10,9,15] )
# print(result)