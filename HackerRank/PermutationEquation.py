def sequenceEquation(p):
    # Write your code here
    opt = []
    for x in range(1,len(p)+1):
        opt.append( p.index( p.index(x) +1  ) + 1   )
    return opt

res = sequenceEquation([4,3,5,1,2])
print(res)
