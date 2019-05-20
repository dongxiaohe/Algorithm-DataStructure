class Solution:
    def jump(self, nums):
        start, maxSteps, steps, newMaxSteps = 0, 0, 0, 0
        if len(nums) == 1: return 0
        while True:
            steps += 1
            for i in range(start, maxSteps + 1):
                newMaxSteps = max(newMaxSteps, nums[i] + i)
                if newMaxSteps >= len(nums) - 1: return steps
            start = maxSteps + 1
            maxSteps = newMaxSteps
        return steps

