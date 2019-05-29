class Solution(object):
    def maxProfit(self, prices):
        if not prices: return 0
        maxCur, maxSoFar = 0, 0
        for i in range(1, len(prices)):
            maxCur += prices[i] - prices[i - 1]
            maxCur = max(0, maxCur)
            maxSoFar = max(maxSoFar, maxCur)
        return maxSoFar
print(Solution().maxProfit( [7,1,5,2,6,4]))
