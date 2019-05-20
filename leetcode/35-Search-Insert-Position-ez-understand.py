class Solution(object):
    def searchInsert(self, nums, target):
        if not nums: return 0
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target: return mid
            if nums[mid] > target: end = mid
            else: start = mid + 1 
        return start + 1 if start == len(nums) - 1 and target > nums[len(nums) - 1] else start

