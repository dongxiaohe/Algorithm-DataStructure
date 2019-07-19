class Solution(object):
    def maxSubArrayLen(self, nums, k):
        preSumMap = collections.defaultdict(int)
        _sum, result = 0, 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum == k: result = i + 1
            elif _sum - k in preSumMap: result = max(result, i - preSumMap[_sum - k])
            if _sum not in preSumMap: preSumMap[_sum] = i
        return result
