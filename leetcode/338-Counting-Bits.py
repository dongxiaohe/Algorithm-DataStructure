class Solution:
    def countBits(self, num):
        dp = [0] * (num + 1)
        for i in range(num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

