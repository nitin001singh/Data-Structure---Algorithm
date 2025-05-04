def kaprekar(p,q):
    flag = False
    for x in range(p, q+1):
        squareNum = str(x * x)
        squareNum = "0"+squareNum if int(squareNum) <= 9 else squareNum
        n = len(squareNum)
        mid = n // 2 
        firstPart = squareNum[:mid] 
        secondPart = squareNum[mid:]
        if int(firstPart) + int(secondPart) ==int(x):
            print(x, end=" ")
            flag = True
            
    if not flag :
        print("INVALID RANGE")

        
    
res = kaprekar(400,700)
print(res)
