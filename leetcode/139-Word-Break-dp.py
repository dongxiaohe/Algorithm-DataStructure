class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict: dp[i] = True
        return dp[len(s)]
