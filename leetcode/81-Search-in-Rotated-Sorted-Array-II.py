class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target: return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]: high = mid - 1
                else: low = mid + 1
            else:
                if nums[mid] < target <= nums[high]: low = mid + 1
                else: high = mid - 1
        return False

print(Solution().search([2,5,6,0,0,1,2], 0))
print(Solution().search([2,5,6,0,0,1,2], 3))
print(Solution().search([1,3,1,1,1], 3))
print(Solution().search([2,5,6,0,0,1,2], 3))
