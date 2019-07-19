class Solution:
    def lengthOfLIS(self, nums):
        m = len(nums)
        if m == 0: return 0
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):  
                if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) 
