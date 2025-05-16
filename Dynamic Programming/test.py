class Solution:
    # We are given an array of integers(a[n]) . We are given multiple queries of the form : (1, i) which means we need to output the sum of all numbers from index- ‘1’ to index ‘i’ of the array.

    def answer1(self, arr, query):
        n = len(arr)
        dp = [0] * (n + 1)
        
        for i in range(n):
            if i == 0:
                dp[i] = arr[i]
            else:
                dp[i] = dp[i-1] + arr[i]
                
        
        for q in query:
            print(dp[q])
        
    # "Given an array of integers(positive as well as negative) ,select some elements from this array(select a subset) such that:-
    # 1. Sum of those elements is maximum(Sum of the subset is maximum) .
    # 2. No two elements in the subset should be consecutive."   
    
   
    def answer2(self, arr):
        n = len(arr)
        dp = [0] * n
        dp[0] = max(arr[0], 0)
        dp[1] = max(arr[1], dp[0])
        # print(dp)
        i = 2
        while i < n:
            dp[i] = max( dp[i - 1],  arr[i] + dp[i - 2] )
            i += 1

        return dp[-1]
    

    # "We are given ‘2’ arrays . Select some elements from both of these arrays (select a subset) such that:-

    # --->1. Sum of those elements is maximum(Sum of the subset is maximum).

    # --->2. No 2 elements in the subset should be consecutive.(Note:-If you select, say the 5th element from Array-1, then you are not allowed to select 4th element from either Array-1 or Array-2 nor are you allowed to select the 5th element from Array -2 all of them are considered consecutive :-) )"

    def answer3(self, arr1, arr2):
        n = len(arr1)
        dp = [0] * n
        
        dp[0] = max(arr1[0], arr2[0])
        dp[1] = max(max(arr1[1], arr2[1]), dp[0])

        i = 2
        while i < n:
            x = dp[i - 1]
            y = arr1[i] + dp[i-2]
            z = arr2[i] + dp[i-2]
            
            dp[i] = max(x,y,z)
            i += 1

        return dp[-1]



    # Frog 1  Atcoder
    
    def answer3(self):
        n = int(input())
        arr = list(map(int, input().split()))

        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(arr[0] - arr[1])

        for i in range(2, n):
            dp[i] = min(
                dp[i - 1] + abs(arr[i] - arr[i - 1]),
                dp[i - 2] + abs(arr[i] - arr[i - 2])
            )

        print(dp[-1]) 
        
        # Frog 2  Atcoder
    
    def answer4(self):
        
        narr = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        
        n = narr[0]
        k = narr[1]

        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(arr[0] - arr[1])

        for i in range(2, n):
            answer = float('inf')
            j = 1
            while j <= k and i - j >= 1:
                yy = dp[i - j] + abs(arr[i] - arr[i - j])
                answer = min(answer, yy)
                j += 1
            dp[i] = answer
            i += 1


        print(dp[-1]) 
        
    def answer5(self, word, k):
        n = len(word)
        dp = [0] * n
        dp[0] = 1
        
        max_len = 1 
        max_index = 0

        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i - 1])) <= k:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
    
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
    
        start_index = max_index - max_len + 1
        print(word[start_index:start_index + max_len])
        
            
# result = Solution().answer1( [6, 7, 3, 2, 2],  [0, 3, 4, 2] )
# result = Solution().answer2( [2,4,6,7,8] )
# result = Solution().answer3( [1,5,3,21234],[-4509 ,200,3,40] )
# result = Solution().answer3()
# result = Solution().answer4()
result = Solution().answer5('bbbbb',2) 
print(result)



