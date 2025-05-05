def stones(n, a, b):
    # Write your code here 
    hashset = set()
    
    for x in range(n):
        hashset.add( b*x + a * (n-x-1) )
        
    return sorted(hashset)

        
    
res = stones(4,10,100)
print(res)
