class Solution:
    def longestConsecutive(self, nums):
        numsSet, best = set(nums), 0
        for x in numsSet:
            if x - 1 not in numsSet:
                y = x + 1
                while y in numsSet: y += 1
                best = max(best, y - x)
        return best
