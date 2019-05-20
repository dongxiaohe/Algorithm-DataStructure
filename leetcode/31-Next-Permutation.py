class Solution(object):
    def nextPermutation(self, nums):
        m = len(nums)
        if m < 2: return
        i = m - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                j = 1
                while i + j + 1 < m and nums[i + j + 1] > nums[i]:
                    j += 1
                nums[i], nums[i + j] = nums[i + j], nums[i]
                nums[i + 1:] = reversed(nums[i + 1:])
                return
            i -= 1
        nums.reverse()
