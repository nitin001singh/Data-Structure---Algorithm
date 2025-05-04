def dayOfProgrammer(year):
    daysinMonths = [31,28,31,30,31,30,31,31]    # Till August
    totalDays = sum(daysinMonths)
    if year <= 1918:
        if year % 4 == 0:
            totalDays += 1        
    else:
        
        if (year % 400 == 0) or ( year % 100 != 0 and year % 4 == 0 ):
            totalDays += 1
            
    programmerDay = 256 - totalDays
    if year == 1918:
        programmerDay = 26
        
    return '0' + str(programmerDay) if programmerDay < 9 else str(programmerDay) + ".09." + str(year)
            
    
    
res = dayOfProgrammer(1918)
print(res)