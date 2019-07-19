class Solution(object):
    def findClosestElements(self, arr, k, x):
        start, end = 0, len(arr) - k
        while start < end:
            mid = start + ((end - start) >> 1)
            if x - arr[mid] > arr[mid + k] - x: start = mid + 1
            else: end = mid
        return arr[start: start + k]

