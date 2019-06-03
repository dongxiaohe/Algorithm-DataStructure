class Solution(object):
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, count, cur = (left + right) >> 1, 1, 0
            for weight in weights:
                if weight + cur > mid:
                    count += 1
                    cur = 0
                cur += weight
            if count > D: left = mid + 1
            else: right = mid
        return left
