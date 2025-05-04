def cutTheSticks(arr):
    # Write your code here
    n = len(arr)
    opt = []
    opt.append(n)
    while n >= 1:
        minVal = min(arr)
        arr = [x for x in arr if x != minVal]
        n = len(arr)
        if n > 0:
            opt.append(n)
        # print(minVal, arr)
        
    return opt

        

    

res = cutTheSticks([8 ,8 ,14, 10, 3 ,5 ,14 ,12])
print(res)
