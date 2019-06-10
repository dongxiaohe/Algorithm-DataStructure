class Solution(object):
    def sortedSquares(self, A):
        position = bisect.bisect(A, 0)
        left, right = position - 1, position
        result = []
        while left >= 0 and right < len(A):
            if abs(A[left]) < abs(A[right]):
                result.append(A[left] ** 2)
                left -= 1
            else:
                result.append(A[right] ** 2)
                right += 1
        while left >= 0:
            result.append(A[left] ** 2)
            left -= 1
        while right < len(A):
            result.append(A[right] ** 2)
            right += 1
        return result
