def getPermutation(n, k):
    result = []
    count = [0]

    def permute(path, used):
        if len(path) == n:
            count[0] += 1
            if count[0] == k:
                result.append("".join(path))
            return

        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                path.append(str(i))
                permute(path, used)
                path.pop()
                used[i] = False
                if result:
                    return

    used = [False] * (n + 1)
    permute([], used)
    return result[0] if result else ""

# Sample Inputs
print(getPermutation(3, 3))
print(getPermutation(4, 9))
