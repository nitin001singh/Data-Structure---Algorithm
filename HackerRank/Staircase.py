def staircase(n):
    for row in range(n):
        for col in range(n-row-1):
            print(" ", end="")
        
        for col in range(row+1):
            print("#", end="")
        
        print()
            
res = staircase(4)
# print(res)


# ---#
# --##
# -###
# ####