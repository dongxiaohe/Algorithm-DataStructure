class Solution(object):
    def peakIndexInMountainArray(self, A):
        start, end = 0, len(A) - 1
        while start < end:
            mid = start + ((end - start) >> 1)
            if A[mid] > A[mid + 1]: end = mid
            else: start = mid + 1
        return start

