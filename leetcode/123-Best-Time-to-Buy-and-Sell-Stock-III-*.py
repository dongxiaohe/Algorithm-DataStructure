class Solution:
    def maxProfit(self, prices):
        buy1, buy2, sell1, sell2 = float("inf"), float("inf"), 0, 0
        for each in prices:
            buy1 = min(buy1, each)
            sell1 = max(sell1, each - buy1)
            buy2 = min(buy2, each - sell1)
            sell2 = max(sell2, each - buy2)
            print(buy1, sell1, buy2, sell2)
        return sell2
print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))
