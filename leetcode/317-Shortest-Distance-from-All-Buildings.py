class Solution(object):
    def shortestDistance(self, grid):
        buildings = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: buildings += 1
        distSum = [[0 for _ in range(n)] for _ in range(m)]
        hits = [[0 for _ in range(n)] for _ in range(m)]
        def bfs(i, j, m, n, buildings):
            count = 1
            level = [(i, j, 1)]
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[i][j] = True # bug free
            while level:
                newLevel = []
                for _i, _j, dist in level:
                    positions = [(_i + 1, _j), (_i - 1, _j), (_i, _j + 1), (_i, _j - 1)]
                    for x, y in positions:                   
                        if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                            visited[x][y] = True
                            if grid[x][y] == 1: count += 1
                            elif not grid[x][y]:
                                hits[x][y] += 1
                                distSum[x][y] += dist
                                newLevel.append((x, y, dist + 1))
                level = newLevel
            return count == buildings
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not bfs(i, j, m, n, buildings): 
                    print(hits)
                    return -1
        result = float("inf")
        for i in range(m):
            for j in range(n):
                if hits[i][j] == buildings: result = min(result, distSum[i][j])
        return result if result != float("inf") else -1 # bug free

