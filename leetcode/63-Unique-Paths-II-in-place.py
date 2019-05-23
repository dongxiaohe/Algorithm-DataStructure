class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0: return 0
        n = len(obstacleGrid[0])
        foundRowObstacle = False
        foundColumnObstacle = False
        if obstacleGrid[0][0] == 1: return 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                        foundColumnObstacle = True
                    elif not foundColumnObstacle:
                        obstacleGrid[i][j] = 1
                elif i == 0:
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                        foundRowObstacle = True
                    elif not foundRowObstacle:
                        obstacleGrid[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[m - 1][n - 1]

