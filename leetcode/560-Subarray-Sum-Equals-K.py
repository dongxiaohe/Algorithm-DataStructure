class Solution(object):
    def subarraySum(self, nums, k):
        map_sum, result, _sum = collections.defaultdict(int), 0, 0
        map_sum[0] = 1
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum - k in map_sum:
                result += map_sum[_sum - k]
            map_sum[_sum] += 1
        return result

