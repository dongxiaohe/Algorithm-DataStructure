class Solution:
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] <= nums[end]: return nums[start]
            mid = start + ((end - start) >> 1)
            if nums[start] <= nums[mid]: start = mid + 1
            else: end = mid

