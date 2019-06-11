class Solution:
    def numIslands(self, grid):
        def dfs(grid, i, j, m, n):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1": return
            grid[i][j] = "0"
            dfs(grid, i + 1, j, m, n)
            dfs(grid, i - 1, j, m, n)
            dfs(grid, i, j + 1, m, n)
            dfs(grid, i, j - 1, m, n)
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j, m, n)
                    counter += 1
        return counter     
