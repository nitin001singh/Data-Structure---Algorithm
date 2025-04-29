
# 13579
# 35791
# 57913
# 79135
# 91357

# N = 5
# odds = [i for i in range(1, 2*N, 2)] 
# for i in range(N):
#     for j in range(N):
#         # print(i, j)
#         print(odds[(i + j) % N], end="")
#     print()




# ******
# *   *
# *  *
# * *
# **
# *

# n = 6
# for i in range(n):
#     for j in range(n - i):
#         if i == 0 or j == 0 or j == n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()





# ******
# *****
# ****
# ***
# **
# *

# n = 6
# for i in range(n):
#     for j in range(n - i):
#         print("*", end=" ")
#     print()



# 1=1
# 1+2=3
# 1+2+3=6
# 1+2+3+4=10
# 1+2+3+4+5=15

# n = 5
# for x in range(1,n+1):
#   summ = 0
#   for y in range(x):
#     res = str(y + 1)
#     print(res, end="")
#     if y < x-1:
#       print("+",end="")
#     summ += y+1
#   print("=" + str(summ), end="")
   
#   print()



# * * * *
#   * * * *
#     * * * *
#       * * * *
      
# n = 4
# for x in range(n):
#   for z in range(x):
#     print(' ', end="")
    
#   for y in range(n):
#     print('*',end="")
  
#   print()




# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

# n = 4
# for x in range(2*n-1):
#     for y in range(2*n-1):
#         top = x
#         left = y
#         right = 2*n-2 - y
#         down = 2*n - 2 - x    
        
#         # print(top, left , right, down)
        
#         print( n - min( min(top, down) , min(right, left)  ) , end=" ")
#     print()









# print left right digonal

# arr=[[1,2,3],[4,5,6],[7,8,9]]
# m = len(arr)
# n = len(arr[0])
# for i in range(m):
#     for j in range(n):
#         if i == j:
#             print(arr[i][j], end=" ")
    
# print('-'*20)
# for i in range(m):
#     for j in range(n):
#         if (i + j)  == m -1:
#             print(arr[i][j], end=" ")



# Print only boudaries 

# 1 2 3 4
# 5 6 7 8
# 9 1 2 3
# 4 5 6 7

# arr=[[1,2,3,4],[4,5,6,7],[2,2,2,2],[7,8,9,10]]
# m = len(arr)
# n = len(arr[0])

# print('-'*20)
# for i in range(m):
#     for j in range(n):
#         if (i == 0 or i == m-1) or (j == 0 or j == n-1):
#             print(arr[i][j], end=" ")
            
            
      
# Z shape matrix      
            
  #  0 1 2 3            
# 0  1 2 3 4
# 1      7 
# 2    1
# 3  4 5 6 7


# arr=[[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
# arr=[[1,2,3],[4,5,6],[7,8,9]]
# m = len(arr)
# n = len(arr[0])

# print('-'*20)
# for i in range(m):
#     for j in range(n):
#         if (i == 0 or i == m-1) or (j == n -1 - i) :
#             print(arr[i][j], end=" ")




# Transpose 

# 1 2 3               1 4 7
# 4 5 6     ===>>     2 5 8
# 7 8 9               3 6 9



# arr=[[1,2,3],[4,5,6],[7,8,9]]
# m = len(arr)
# n = len(arr[0])

# print('-'*20)
# for i in range(m):
#     for j in range(n):
#             print(arr[j][i], end=" ")
#     print("")


# Matrix in Snake Shape

# arr=[[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]
# m = len(arr)
# n = len(arr[0])

# print('-'*20)
# for i in range(m):
#     if i%2 ==0:
#         for j in range(n):
#                 print(arr[i][j], end=" ")
#     else:
#         for j in range(n-1,-1,-1):
#                 print(arr[i][j], end=" ")
#     print("")

