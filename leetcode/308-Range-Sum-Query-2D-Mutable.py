class NumMatrix(object):

    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        self.nums = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        if self.m == 0 or self.n == 0: return
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                # print(i, j)
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def sum(self, row, col):
        _sum = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                _sum += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return _sum

    def sumRegion(self, row1, col1, row2, col2):
        if self.m == 0 or self.n == 0: return 0
        return self.sum(row2 + 1, col2 + 1) + self.sum(row1, col1) - self.sum(row1, col2 + 1) - self.sum(row2 + 1, col1)

