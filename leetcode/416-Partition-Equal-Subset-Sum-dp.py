class Solution:
    def canPartition(self, nums):
        total, n = sum(nums), len(nums)
        if total & 1 == 1: return False
        half = total >> 1
        matrix = [[0 for _ in range(half + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, half + 1):
                if i == 0: 
                    if j >= nums[i]: matrix[i][j] = nums[i]
                    else: matrix[i][j] = 0
                else:
                    if j >= nums[i]:
                        matrix[i][j] = max(matrix[i - 1][j], nums[i] + matrix[i - 1][j - nums[i]])
                    else: matrix[i][j] = matrix[i - 1][j]
                if matrix[i][j] == half: return True
        return False
