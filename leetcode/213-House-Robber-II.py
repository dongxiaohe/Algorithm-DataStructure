"""
      1, 5, 2, 3, 4, 7
incl  1, 5, 3, 8, 9, 15
excl  0, 1, 5, 5, 8, 9

_incl 0, 5, 2, 8, 9, 15
_excl 0, 0, 5, 5, 8, 9

"""
class Solution:
    def rob(self, nums):
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        incl, excl, _incl, _excl = nums[0], 0, 0, 0
        for i in range(1, n):
            tmpExcl = max(incl, excl)
            incl = excl + nums[i]
            excl = tmpExcl
            _tmpExcl = max(_incl, _excl)
            _incl = _excl + nums[i]
            _excl = _tmpExcl
        return max(excl, _incl, _excl)
