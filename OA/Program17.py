class Solution:
    def answer(self, a, x, y):
        n = len(a)
        pref = [0] * n
        
        # Compute y-stepped prefix sum
        for i in range(n):
            if i - y >= 0:
                pref[i] = a[i] + pref[i - y]
            else:
                pref[i] = a[i]

        k = float('inf')
        
        # Find minimum sum of x elements with y-step ending at i
        for i in range(n):
            index = i - (x - 1) * y
            if index >= 0:
                g = pref[i]
                if index - y >= 0:
                    g -= pref[index - y]
                k = min(g, k)
                print(f"Sum from index {index} to {i} with step {y}: {g}")

        print("Minimum sum:", k)
        return k



result = Solution().answer([5,2,3,4,6,2,1,6,4,3,2],2,3)
print(result) 