# Brute Force

# TC : O(n*k)
# SC : O(1)

# def answer(arr , k):
#     n = len(arr)
#     for i in range(n-k+1):
#         summ = 0
#         for j in range(i, i+k):
#             summ += arr[j]
            
#         print(summ)


# res = answer([1,2,3,4,5,6], 3)



# Optimal

# TC : O(N)
# SC : O(1)


def answer(arr , k):
    n = len(arr)
    summ = 0
    for i in range(k):
        summ += arr[i]
    print(summ)
    for i in range(k, n):
        summ =  (summ - arr[i-k]) +  arr[i]
            
        print(summ)


res = answer([1,2,3,4,5,6], 3)