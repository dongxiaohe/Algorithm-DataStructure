class Solution:
    def singleNumber(self, nums):
        diff = 0
        for n in nums:  diff ^= n
        diff &= -diff
        a, b = 0, 0
        for n in nums:
            if n & diff == 0: a ^= n
            else: b ^= n
        return [a, b]
