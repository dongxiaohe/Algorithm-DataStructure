class Solution:
    def combinationSum2(self, candidates, target):
        def _sum(candidates, target, start, n, acc, result):
            if target < 0: return
            elif target == 0:
                result.append(acc)
                return
            for i in range(start, n): 
                if target < candidates[i]: return
                if i > start and candidates[i] == candidates[i - 1]: continue
                _sum(candidates, target - candidates[i], i + 1, n, acc + [candidates[i]], result)
        result = [] 
        candidates.sort()
        n = len(candidates)
        _sum(candidates, target, 0, n, [], result)
        return result
