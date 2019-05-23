class Solution(object):
    def mySqrt(self, x):
        if x == 1: return 1
        start, end = 0, x >> 1
        while start <= end:
            mid = start + ((end- start) >> 1)
            power = mid ** 2
            if power == x: return mid
            elif power < x: start = mid + 1
            else: end = mid - 1
        return start - 1
