class Solution:
    def maxSubArray(self, nums):
        tmpMax, totalMax, n = nums[0], nums[0], len(nums)
        for i in range(1, n):
            tmpMax = max(tmpMax + nums[i], nums[i])
            totalMax = max(tmpMax, totalMax)
        return totalMax
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
