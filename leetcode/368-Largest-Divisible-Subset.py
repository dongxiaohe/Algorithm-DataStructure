class Solution:
    def largestDivisibleSubset(self, nums):
        nums, m = sorted(nums), len(nums)
        if m == 0: return []
        dp = [[] for i in range(m)]
        dp[0] = [nums[0]]
        for i in range(1, m):
            tmp = []
            for j in range(i - 1, -1, -1):
                if j >= 0:
                    if nums[i] % nums[j] == 0:
                        tmp = max(tmp, dp[j], key = len)
                if j == 0:
                    dp[i] += tmp + [nums[i]]
        maxCount, result = 0, []
        for t in dp:
            n = len(t)
            if n > maxCount:
                result = t
                maxCount = n
        return result
