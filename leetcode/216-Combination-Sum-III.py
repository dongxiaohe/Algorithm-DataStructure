class Solution:
    def combinationSum3(self, k, n):
        def backtrack(nums, start, k, n, acc, result):
            if n == 0 and len(acc) == k: 
                result.append(acc)
                return
            if n < 0: return
            for i in range(start, len(nums)):
                backtrack(nums, i + 1, k, n - nums[i], acc + [nums[i]], result)
        result = []
        backtrack(list(range(1, 10)), 0, k, n, [], result)
        return result
print(Solution().combinationSum3(3, 7)) 
