class Solution:
    def canJump(self, nums):
        n = len(nums)
        lastPoint = n - 1
        for i in range(lastPoint, -1 , -1):
            if i + nums[i] >= lastPoint:
                lastPoint = i
        return lastPoint == 0
