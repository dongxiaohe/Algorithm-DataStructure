class Solution:
    def combine(self, n, k):
        def _combinations(k, start, end, acc, result):
            if k == 0:
                result.append(acc)
                return
            for i in range(start, end):
                _combinations(k - 1, i + 1, end, acc + [i], result)
        result = []
        _combinations(k, 1, n + 1, [], result)
        return result

