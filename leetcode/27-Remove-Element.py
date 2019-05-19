class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        if n == 0: return 0
        i = 0
        while i < n:
            if nums[i] == val:
                nums.remove(nums[i])
                n = n - 1
            else: i += 1
        return n

