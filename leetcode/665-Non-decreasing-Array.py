class Solution(object):
    def checkPossibility(self, nums):
        counter, i, n = 0, 0, len(nums)
        if n <= 1: return True
        while i < n - 1 and counter <= 1:
            if nums[i] > nums[i + 1]:
                counter += 1
                if i - 1 >= 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
            i += 1
        return counter <= 1
