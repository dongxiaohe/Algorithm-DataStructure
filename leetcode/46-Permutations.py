class Solution:
    def permute(self, nums):
        def _permute(nums, acc, result, n, visited):
            if len(acc) == n:
                result.append(acc)
                return 
            for i in range(n):
                if visited[i]: continue
                visited[i] = True
                _permute(nums, acc + [nums[i]], result, n, visited)
                visited[i] = False
        result = []
        visited = [False for _ in range(len(nums))]
        _permute(nums, [], result, len(nums), visited)
        return result
