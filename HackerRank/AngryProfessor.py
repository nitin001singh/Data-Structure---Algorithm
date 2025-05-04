def angryProfessor(k,a):
    
    arrivalOnTime = 0
    for x in a:
        if x <= 0:
            arrivalOnTime += 1
            
    return 'NO' if arrivalOnTime >= k else "YES"  
    
res = angryProfessor(3, [-2,-1,0,1,2])
print(res) 