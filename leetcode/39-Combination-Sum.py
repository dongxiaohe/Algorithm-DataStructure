class Solution:
    def combinationSum(self, candidates, target):
        def _accumulateSum(candidates, target, n, acc, result, start):
            if target < 0:
                return
            elif target == 0:
                result.append(acc)
                return
            else: 
                for i in range(start, n):
                    if candidates[i] > target:
                        return
                    else:
                        _accumulateSum(candidates, target - candidates[i], n, acc + [candidates[i]], result, i)
        candidates.sort()
        result = []
        _accumulateSum(candidates, target, len(candidates), [], result, 0)
        return result
print(Solution().combinationSum([2,3,6,7], 7))
