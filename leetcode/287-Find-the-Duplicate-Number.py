class Solution:
    def findDuplicate(self, nums):
        from functools import reduce
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            total = reduce(lambda acc, t: acc + int(t <= mid), nums, 0)
            # print(left, total)
            if total <= mid: left = mid + 1
            else: right = mid
        return right

print(Solution().findDuplicate([1,2,2,6,3,4,5]))
print(Solution().findDuplicate([1,3,3,6,2,4,5]))
