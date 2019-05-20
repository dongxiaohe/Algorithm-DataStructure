class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        if not nums: return result
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + ((end - start) >> 1)
            if nums[mid] < target: start = mid + 1
            else: end = mid
        if nums[start] != target: return result
        result[0], end = start, len(nums) - 1
        while start < end:
            mid = start + ((end - start) >> 1) + 1
            if nums[mid] > target: end = mid - 1
            else: start = mid
        result[1] = end
        return result
