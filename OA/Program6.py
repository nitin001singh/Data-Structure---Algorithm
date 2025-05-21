
# TC : O(N + 1440 + 1440)   =>  O(N)
# SC : O(1440)   = > O(1)


class Solution:
    
    def answer(self, actionList, k):
        
        total_minute_per_Day = 1440
        timearr = [0] * total_minute_per_Day
        for action in actionList:
            data = action.split()
            start = self.convertToMinute(data[2])
            end = self.convertToMinute(data[3])
            
            
            
            timearr[start] += 1 
            timearr[end + 1] -= 1
            
            
        for index in range(1, len(timearr)):
            timearr[index] = timearr[index - 1] + timearr[index]


        c = 0
        ans = 0
        g = 1
        for x in range(total_minute_per_Day):
            if timearr[x] == 0:
                c += 1
                
                if c == k:
                    ans = self.showToHourMinute((x - k + 1))
                    g = 0
                    break
                
        
     
        if g == 1:
            return -1
        
        return ans
    
    def convertToMinute(self , val):
        hour, minute = map(int, val.split(":"))
        return ((int(hour) * 60) + minute)
    
    def showToHourMinute(self , val):
        
        hour = val // 60
        minute = val % 60
        
        return f"{hour:02d}" + ":" + f"{minute:02d}"
        

result = Solution().answer( ["Alex sleeps 00:00 08:00", "Sam sleeps 07:00 13:00", "Alex lunch 12:30 13:59"] , 60 )
print(result)