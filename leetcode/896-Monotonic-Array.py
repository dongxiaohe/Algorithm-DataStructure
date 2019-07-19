class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True
        for i in range(1, len(A)):
            if A[i - 1] < A[i]: decreasing = False
            if A[i - 1] > A[i]: increasing = False
            if not decreasing and not increasing: return False
        return True

