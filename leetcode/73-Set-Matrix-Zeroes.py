class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        cols = False
        for i in range(m):
            if matrix[i][0] == 0: cols = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if cols: matrix[i][0] = 0
