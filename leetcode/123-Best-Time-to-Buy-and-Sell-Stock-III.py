class Solution(object):
    def maxProfit(self, prices):
        if not prices: return 0
        k, days = 3, len(prices)
        dp = [[0 for _ in range(days)] for _ in range(k)]
        for i in range(1, k):
            maxDiff = dp[i - 1][0] - prices[0]
            for j in range(1, days):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff) 
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])
        return dp[k - 1][days - 1]

print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))
