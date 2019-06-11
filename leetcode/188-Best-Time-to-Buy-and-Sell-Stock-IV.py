class Solution:
    def maxProfit(self, k, prices):
        def quickProfit(prices):
            maxCur = 0
            for i in range(len(prices) - 1):
                maxCur += max(0, prices[i + 1] - prices[i])
            return maxCur
        m = len(prices)
        if k > (m >> 1): return quickProfit(prices)
        if m == 0: return 0
        dp = [[0 for _ in range(m)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxDiff, maxCur = float("-inf"), 0
            for j in range(1, m):
                maxDiff = max(maxDiff, dp[i - 1][j - 1] - prices[j - 1]) #since price[j] is a constant
                maxCur = max(maxCur, dp[i][j - 1], prices[j] + maxDiff)
                dp[i][j] = maxCur
        return dp[k][m - 1]

    def generalApproach(self, k, prices):
        """
        dp[k][m] m stands of length of prices
            3, 2, 6, 5, 0, 3
        0   0  0  0  0  0  0
        1   0  0  4  4  4  4
        2   0  0  4  4  0  7

        dp[i][j] = max(dp[i - 1][j], prices[j] - prices[i] + dp[i - 1][j] ...) i is from 0 to j
        """
        m = len(prices)
        if m == 0: return 0
        dp = [[0 for _ in range(m)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(1, m):
                maxCur = 0
                for t in range(j):
                    maxCur = max(maxCur, dp[i][j - 1], prices[j] - prices[t] + dp[i - 1][t])
                dp[i][j] = maxCur
        return dp[k][m - 1]
