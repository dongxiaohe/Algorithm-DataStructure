class Solution:
    def uniquePaths(self, m, n):
        if n > m: return self.uniquePaths(n, m)
        if n <= 1: return 1
        totalSteps, numerator, denominator = m + n - 2, 1, 1
        for i in range(1, n):
            denominator *= i
            numerator *= totalSteps + 1 - i 
        return numerator // denominator
            

print(Solution().uniquePaths(7, 3))
print(Solution().uniquePaths(4, 4))
print(Solution().uniquePaths(7, 5))
