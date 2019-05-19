class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        start, end = 0, m
        while start <= end:
            partitionX = start + ((end - start) >> 1)
            partitionY = ((m + n + 1) >> 1) - partitionX
            x1 = nums1[partitionX - 1] if partitionX != 0 else float("-inf")
            x2 = nums1[partitionX] if partitionX != m else float("inf")
            y1 = nums2[partitionY - 1] if partitionY != 0 else float("-inf")
            y2 = nums2[partitionY] if partitionY != n else float("inf")
            if x1 <= y2 and y1 <= x2:
                if m + n & 1 == 1: return max(x1, y1)
                return float(max(x1, y1) + min(x2, y2)) / 2
            elif x1 <= y2: start = partitionX + 1
            else: end = partitionX - 1
