class Solution:
    def rob(self, nums):
        def dp(nums, start, n, mem):
            if start >= n: return 0
            if n == start + 1: return nums[start]
            if start in mem: return mem[start]
            res = max(nums[start] + dp(nums, start + 2, n, mem), dp(nums, start + 1, n, mem))
            mem[start] = res
            return res
        return dp(nums, 0, len(nums), {})
