class Solution:
    def fourSum(self, nums, target):
        def findNSum(nums, n, target, acc, result):
            numsLength = len(nums)
            if numsLength < n or n < 2 or target < nums[0] * n or target > nums[-1] * n:
                return
            if n == 2:
                left, right = 0, numsLength - 1
                while left < right: 
                    total = nums[left] + nums[right]
                    if total == target:
                        result.append(acc + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(numsLength - n + 1):
                    if i == 0 or nums[i] != nums[i - 1]:
                        findNSum(nums[i + 1:], n - 1, target - nums[i], acc + [nums[i]], result)
        result = []
        nums.sort()
        findNSum(nums, 4, target, [], result)
        return result
