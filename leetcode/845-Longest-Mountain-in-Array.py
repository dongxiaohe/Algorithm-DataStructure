class Solution(object):
    def longestMountain(self, A):
        left, right, result = 0, len(A), 0
        while left < right:
            base = left
            if base + 1 < right and A[base] < A[base + 1]:
                while base + 1 < right and A[base] < A[base + 1]:
                    base += 1
                if base + 1 < right and A[base] > A[base + 1]:
                    while base + 1 < right and A[base] > A[base + 1]:
                        base += 1
                    result = max(result, base - left + 1)
            left = max(base, left + 1)
        return result

