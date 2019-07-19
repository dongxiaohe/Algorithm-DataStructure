class Solution:
    def kthSmallest(self, matrix, k):
        def countLessThan(mid):
            i, j, count = n - 1, 0, 0
            while i >= 0 and j < n:
                if matrix[i][j] > mid: i -= 1
                else:
                    j += 1
                    count += i + 1
            return count
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        while low <= high:
            mid = (low + high) >> 1
            count = countLessThan(mid)
            if count < k: low = mid + 1
            else: high = mid - 1
        return low   
        
