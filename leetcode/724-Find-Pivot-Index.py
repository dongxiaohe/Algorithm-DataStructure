class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        acc = 0
        for i, number in enumerate(nums):
            if total - number - acc == acc: return i
            acc += number
        return -1

