class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start, end = 0, len(letters) - 1
        while start < end:
            mid = start + ((end - start) >> 1)
            if letters[mid] > target: end = mid
            else: start = mid + 1
        return letters[0] if start == len(letters) - 1 and target >= letters[-1] else letters[start]

