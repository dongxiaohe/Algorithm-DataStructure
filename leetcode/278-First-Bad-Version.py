class Solution:
    def firstBadVersion(self, n):
        start = 0
        while start < n:
            mid = start + ((n - start) >> 1)
            if isBadVersion(mid): n = mid
            else: start = mid + 1
        return start

