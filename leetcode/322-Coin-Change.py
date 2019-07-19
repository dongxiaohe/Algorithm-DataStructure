class Solution:
    def coinChange(self, coins, amount):
        def dp(coins, amount, mem):
            if amount < 0: return -1
            if amount == 0: return 0
            if amount in mem: return mem[amount]
            minVal = float("inf")
            for coin in coins:
                res = dp(coins, amount - coin, mem)
                if res >= 0: minVal = min(1 + res, minVal)
            mem[amount] = minVal if minVal != float("inf") else -1
            return mem[amount]
        mem = {}
        return dp(coins, amount, mem)

