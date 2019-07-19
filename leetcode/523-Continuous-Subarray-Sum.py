class Solution(object):
    def checkSubarraySum(self, nums, k):
        sumMap = collections.defaultdict(int)
        sumMap[0] = -1 # bug free
        runningSum = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            if k != 0: runningSum %= k
            if runningSum in sumMap:
                prev = sumMap[runningSum]
                if i > prev + 1: return True
            else: sumMap[runningSum] = i
        return False
