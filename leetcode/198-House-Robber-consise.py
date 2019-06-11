"""
     1, 2, 5, 2, 1, 3
incl 1, 2, 6, 4, 7, 9
excl 0, 1, 2, 6, 6, 7

incl[i] = excl[i - 1] + nums[i]
excl[i] = max(incl[i - 1], excl[i - 1])

"""
class Solution:
    def rob(self, nums):
        incl, excl = 0, 0
        for i in range(len(nums)): 
            tmpExcl = max(incl, excl)
            incl = excl + nums[i]
            excl = tmpExcl
        return max(excl, incl)
