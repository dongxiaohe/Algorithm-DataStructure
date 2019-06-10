class Solution:
    def maxProduct(self, nums):
        r = imin = imax = nums[0]
        for i in range(1, len(nums)): # No matterh which first two values are, imax is max value and imin is min value
            if nums[i] < 0: imin, imax = imax, imin
            imin = min(nums[i], imin * nums[i])
            imax = max(nums[i], imax * nums[i])
            r = max(r, imax)
        return r
