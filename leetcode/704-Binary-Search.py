class Solution(object):
    def search(self, nums, target):
        if not nums: return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target: return mid
            elif nums[mid] < target: start = mid + 1
            else: end = mid - 1
        return -1
