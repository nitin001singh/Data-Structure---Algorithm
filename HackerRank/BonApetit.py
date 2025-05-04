def bonAppetit(bill, k, b):
    # Write your code here
    summ = 0
    for index, val in enumerate(bill):
        if index != k:
            summ += val
    # print(summ)
    return  "Bon Appetit" if  (b - summ // 2)  == 0 else b - summ // 2
    
res = bonAppetit([3 ,10 ,2 ,9], 1, 12)
print(res)