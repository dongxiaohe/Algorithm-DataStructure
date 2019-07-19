class Solution(object):
    def arrangeCoins(self, n):
        count, total = 1, 1
        while total <= n:
            count += 1
            total += count 
        return count - 1
