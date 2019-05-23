class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        low, high = 0, m * n - 1
        while low != high:
            mid = (low + high - 1) >> 1
            if matrix[mid // n][mid % n] < target: low = mid + 1
            else: high = mid
        return matrix[high // n][high % n] == target

matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
print(Solution().searchMatrix(matrix, 23))