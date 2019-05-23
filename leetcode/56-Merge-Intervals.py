class Solution:
    def merge(self, intervals):
        result = []
        for interval in sorted(intervals, key = lambda x: x.start):
            if result and result[-1].end >= interval.start:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result += interval
        return result

