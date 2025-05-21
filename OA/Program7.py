
class Solution:
    def answer(self, lamps, points):

        size = 100000    #size: 10^5
        lamp = [0] * size
        
        for l , r in lamps:
            lamp[l] += 1
            lamp[r+1] -= 1

        for x in range(1, len(lamp)):
            lamp[x] = lamp[x-1] + lamp[x]


        for p in points:
            print(lamp[p], end=" ")


result = Solution().answer( [[1,7],[5,11],[7,9]], [7,1,5,10,9,15] )
# print(result)