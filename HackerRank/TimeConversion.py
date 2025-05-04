def timeConversion(s):
    # Write your code here
    if 'PM' in s:
        timeStr = s.replace('PM',"")
        timeList = timeStr.split(":")
        timeList[0] = str((int(timeList[0]) + 12)) if int(timeList[0]) < 12 else timeList[0]
        
    else:
        timeStr = s.replace('AM',"")
        timeList = timeStr.split(":")
        timeList[0] = "00" if int(timeList[0]) == 12 else timeList[0]
        
    
    return ":".join(timeList)
    
res = timeConversion('12:40:22AM')
print(res)