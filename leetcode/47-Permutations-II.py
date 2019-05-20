class Solution:
    def permuteUnique(self, nums):
        def _permute(nums, acc, result, n, used):
            if len(acc) == n:
                result.append(acc)
                return
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]): continue
                used[i] = True
                _permute(nums, acc + [nums[i]], result, n, used)
                used[i] = False
        nums.sort()
        n = len(nums)
        result = []
        used = [False for _ in range(n)]
        _permute(nums, [], result, n, used)
        return result

print(Solution().permuteUnique([1,1,2]))
