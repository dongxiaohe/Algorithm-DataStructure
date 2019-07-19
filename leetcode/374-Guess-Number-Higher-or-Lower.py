class Solution(object):
    def guessNumber(self, n):
        start = 1
        while start <= n:
            mid = start + ((n - start) >> 1)
            if guess(mid) == 0: return mid
            elif guess(mid) == -1: n = mid - 1
            else: start = mid + 1

