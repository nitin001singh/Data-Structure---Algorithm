def chocolateFeast(n, c, m):
    res = n // c
    wrapper = res
    while wrapper >= m :
        temp = wrapper % m 
        wrapper //= m
        res += wrapper
        wrapper += temp
    return res


res = chocolateFeast(15,3,2)
print(res)

