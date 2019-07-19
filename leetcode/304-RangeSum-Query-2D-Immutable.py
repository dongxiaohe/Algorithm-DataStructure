class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0]) if m != 0 else 0
        self._sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self._sum[i][j] = matrix[i - 1][j - 1] + self._sum[i - 1][j] + self._sum[i][j - 1] - self._sum[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        return self._sum[row2 + 1][col2 + 1] - self._sum[row2 + 1][col1] - self._sum[row1][col2 + 1] + self._sum[row1][col1]

