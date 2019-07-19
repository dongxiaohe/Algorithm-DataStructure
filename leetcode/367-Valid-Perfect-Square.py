class Solution(object):
    def isPerfectSquare(self, num):
        if num <= 1: return True
        start, end = 1, num >> 1
        while start <= end:
            mid = start + ((end - start) >> 1)
            power = mid ** 2 
            if power == num: return True
            elif power < num: start = mid + 1
            else: end = mid - 1
        return False
