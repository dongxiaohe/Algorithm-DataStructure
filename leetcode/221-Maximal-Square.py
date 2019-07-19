class Solution:
    def maximalSquare(self, matrix):
        newMatrix = matrix[:]
        m = len(newMatrix)
        if m == 0: return 0
        n, total = len(newMatrix[0]), 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: total = max(total, int(newMatrix[i][j]))
                elif newMatrix[i][j] == "1": newMatrix[i][j] = str(int(newMatrix[i][j]) + min(int(newMatrix[i - 1][j]), int(newMatrix[i][j - 1]), int(newMatrix[i - 1][j - 1])))
                total = max(total, int(newMatrix[i][j]))
        return total ** 2

