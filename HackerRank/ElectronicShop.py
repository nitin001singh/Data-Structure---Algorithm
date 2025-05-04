def getMoneySpent(keyboards, drives, b):
    if not keyboards and not drives:
        return []
    
    opt = []
    for x in keyboards:
        for y in drives:
            if x + y <= b:
                opt.append(x+y)
                
    return max(opt) if opt else -1
            

    
res = getMoneySpent([40,50,60],[5,8,12],60)
print(res)                              
