class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in range(len(nums)):
                if i >= nums[j]: dp[i] += dp[i - nums[j]]
        return dp[target]
"""
nums = [1,2,3], target = 4
      1 2 3
    
i=0 1 0 0 0 0
i=1 1 1 0 0 0
i=2 1 1 2 0 0
i=3 1 1 2 4 0
i=4 1 1 2 4 7
"""
         
