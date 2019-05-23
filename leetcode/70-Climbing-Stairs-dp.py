class Solution:
    def climbStairs(self, n):
        def numSteps(n, steps):
            result = [0] * (n + 1)
            result[0] = 1
            for i in range(1, n + 1):
                total = 0
                for j in steps:
                    if i - j >= 0:
                        total += result[i - j]
                result[i] = total
            return result[n]
        return numSteps(n, [3, 6]) 
# steps = [a, b, c], result[n] = result[n - a] + result[n - b] + result[n - c]
print(Solution().climbStairs(6))
