class Solution(object):
    def smallestDistancePair(self, nums, k):
        def upperBound(arr, low, high, target):
            if arr[high] <= target: return high + 1
            while low < high:
                mid = low + (high - low >> 1)
                if arr[mid] <= target: low = mid + 1
                else: high = mid
            return low
        def countLessThanK(arr, diff):
            count, n = 0, len(arr)
            for i in range(n):
                count += upperBound(arr, i, n - 1, arr[i] + diff) - i - 1
            return count
        nums.sort()
        low = nums[1] - nums[0]
        n = len(nums)
        for i in range(1, n - 1):
            low = min(low, nums[i + 1] - nums[i])
        high = nums[n - 1] - nums[0]
        while low < high:
            mid = low + (high - low >> 1)
            if countLessThanK(nums, mid) < k: low = mid + 1
            else: high = mid
        return low

