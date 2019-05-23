class Solution:
    def subsetsWithDup(self, nums):
        def _backtrack(nums, start, end, acc, result):
            result.append(acc)
            for i in range(start, end):
                if i != start and nums[i] == nums[i - 1]: continue
                _backtrack(nums, i + 1, end, acc + [nums[i]], result)
        nums.sort()
        n, result = len(nums), []
        _backtrack(nums, 0, n, [], result)
        return result
