def combinationSum2(matrix, target):
    result = []
    matrix.sort()

    def getCombination(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        prev = -1
        for i in range(start, len(matrix)):
            if matrix[i] == prev:
                continue
            path.append(matrix[i])
            getCombination(i + 1, path, total + matrix[i])
            path.pop()
            prev = matrix[i]

    getCombination(0, [], 0)
    return result

combinations = combinationSum2( [10, 1, 2, 7, 6, 1, 5], 8)
for combo in combinations:
    print(*combo)
