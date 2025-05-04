def taumBday(b, w, bc, wc, z):
    cost_black = min(bc, wc + z)
    cost_white = min(wc, bc + z)
    return b * cost_black + w * cost_white
    
res = taumBday(10,10,1,1,1)
print(res)
