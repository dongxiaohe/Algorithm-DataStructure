class Solution:
    def coinChange(self, coins, total):
        dp = [float("inf")] * (total + 1)
        dp[0] = 0
        for i in range(1, total + 1):
            for coin in coins:
                if i >= coin: dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[total] if dp[total] != float("inf") else -1

