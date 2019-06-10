class Solution(object):
    def twoSum(self, nums, target):
        if not nums: return -1
        start, end = 0, len(nums) - 1
        while start != end:
            total = nums[start] + nums[end]
            if total == target: return [start + 1, end + 1]
            elif total < target: start += 1
            else: end -= 1