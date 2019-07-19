class Solution:
    def findLengthOfLCIS(self, nums):
        result = start = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i - 1]: start = i
            result = max(result, i - start + 1)
        return result
