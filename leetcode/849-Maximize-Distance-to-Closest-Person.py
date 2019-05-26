class Solution(object):
    def maxDistToClosest(self, seats):
        max_result = 0
        for seat, group in itertools.groupby(seats):
            if seat == 0:
                max_result = max(max_result, len(list(group)) + 1 >> 1)
        return max(max_result, seats.index(1), seats[::-1].index(1))
