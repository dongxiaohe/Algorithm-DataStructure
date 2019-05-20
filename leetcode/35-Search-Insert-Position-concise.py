class Solution:
    def searchInsert(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            print(start, end)
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
print(Solution().searchInsert(range(100), 67))
print(Solution().searchInsert([1,3], 2))
