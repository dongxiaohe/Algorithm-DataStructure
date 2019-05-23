class Solution:
    def subsets(self, nums):
        def _backtrack(list, acc, start, end, result):
            result.append(acc)
            for i in range(start, end):
                _backtrack(list, acc + [list[i]], i + 1, end, result)
        result = []
        _backtrack(nums, [], 0, len(nums), result) 
        return result
