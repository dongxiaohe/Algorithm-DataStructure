class Solution(object):
    def longestIncreasingPath(self, matrix):
        def dfs(matrix, i, j, m, n, directions, visited):
            if visited[(i, j)] != 0: return visited[(i, j)]
            maxLen = 1
            for x, y in directions:
                tmpI, tmpJ = i + x, j + y
                if tmpI < 0 or tmpI >= m or tmpJ < 0 or tmpJ >= n or matrix[tmpI][tmpJ] <= matrix[i][j]: continue
                tmpLen = 1 + dfs(matrix, tmpI, tmpJ, m, n, directions, visited)
                maxLen = max(maxLen, tmpLen)
            visited[(i, j)] = maxLen
            return maxLen
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        maxLen = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen, dfs(matrix, i, j, m, n, directions, visited))
        return maxLen
