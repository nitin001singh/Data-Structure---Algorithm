def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 < x2 :
        if v1 <= v2:
            return "NO"
        else:
            while x1 <= x2:
                if x1 == x2:
                    return "YES"
                x1 += v1
                x2 += v2
                
            return "NO"
        
    else:
        
        if v2 <= v1:
            return "NO"
        else:
            while x2 <= x1:
                if x1 == x2:
                    return "YES"
                x1 += v1
                x2 += v2
                
            return "NO"
            
    return "NO"
    
res = kangaroo(0 ,2, 5, 3)
print(res)