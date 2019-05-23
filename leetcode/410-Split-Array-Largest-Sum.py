class Solution(object):
    def splitArray(self, nums, m):
        lower, higher = max(nums), sum(nums)
        result = higher
        while lower <= higher:
            mid = (lower + higher) >> 1
            count, _sum = 1, 0
            for number in nums:
                if _sum + number > mid:
                    count += 1
                    _sum = number
                else: _sum += number
            if count <= m:
                result = min(result, mid)
                higher = mid - 1
            else: lower = mid + 1
        return result
