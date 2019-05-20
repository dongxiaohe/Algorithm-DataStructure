class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                k = nums[i] - 1
                nums[i], nums[k] = nums[k], nums[i]
        for i in range(n):
            if nums[i] != i + 1: return i + 1
        return n + 1