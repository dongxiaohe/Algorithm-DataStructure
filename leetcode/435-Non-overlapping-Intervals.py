class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) <= 1: return 0
        intervals.sort(key = lambda x: x.end)
        count, end = 1, intervals[0].end
        for t in intervals:
            if t.start >= end:
                end = t.end
                count += 1
        return len(intervals) - count
