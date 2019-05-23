class Solution:
    def merge(self, nums1, m, nums2, n):
        k = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1
        if n >= 0: nums1[:n + 1] = nums2[:n + 1]

