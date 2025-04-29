# 0 0 0 0 0 0 
# 0 0 0 0 0 0
# 0 0 0 0 0 0 
# 0 0 0 0 0 0
# 0 0 0 0 0 0


n = 5
for row in range(n):
    for col in range(6):
        print('0', end=" ")
    print()

print('--' * 30)
    
# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

n = 6
for row in range(n):
    for col in range(1, row+1):
        print(col, end=" ")
    print()


print('--' * 30)       
        
# A 
# B B 
# C C C 
# D D D D 


n = 4
for row in range(n):
    for col in range(row + 1 ):
        print(chr(row+65), end=" ")
    print()
    

print('--' * 30)

# A 
# B C 
# C D E 
# D E F G 


n = 7
for row in range(n):
    for col in range(row + 1):
        print(chr(65 + col+row), end=" ")
    print()


print('--' * 30)


# E
# D E
# C D E
# B C D E
# A B C D E

n = 7
num = ord('A') + n
for x in range(1,n+1):
    for y in range(num - x, num):
        print(chr(y), end=" ")
    print()

print('--' * 30)


#       1 
#     1 2 
#   1 2 3 
# 1 2 3 4

n = 4
for row in range(n):
    for _ in range(n - row - 1):
        print(" ", end=" ")

    for col in range(1, row + 2):
        print(col, end=" ")
    print()
    
print('--' * 30)


# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 

n = 5
for row in range(n):
    for col in range(n - row):
        print(n -row, end=" ")
    print()


print('--' * 30)


# n = 5
# for row in range(n):
#     for col in range(row):
#         print(col, end="")
#     print("")
