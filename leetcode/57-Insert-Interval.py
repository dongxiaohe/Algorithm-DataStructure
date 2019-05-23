class Solution:
    def insert(self, intervals, newInterval):
        result, n, hasInsert  = [], len(intervals), False
        if n == 0: return [newInterval]

        for i in range(n):
            if intervals[i].start <= newInterval.end and newInterval.start <= intervals[i].end:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
            elif newInterval.end < intervals[i].end:
                result.append(newInterval)
                result.extend(intervals[i::])
                hasInsert = True
                break
            else:
                result.append(intervals[i])
        if not hasInsert:
            result.append(newInterval)

        return result

