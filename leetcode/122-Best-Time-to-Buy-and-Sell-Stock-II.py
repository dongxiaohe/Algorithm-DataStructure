class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        maxSoFar = 0
        for i in range(len(prices) - 1):
            maxSoFar += max(0, prices[i + 1] - prices[i])
        return maxSoFar