# BruteForce 

# TC : O(N^3)
# SC : O(1)

def subSequence(arr):
    subsequences = [[]] 
    for num in arr:
        new_subsequences = [seq + [num] for seq in subsequences]
        subsequences.extend(new_subsequences)
    return subsequences


res= subSequence([1, 2, 3, 4])
print(res)
