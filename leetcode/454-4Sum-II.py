class Solution:
    def fourSumCount(self, A, B, C, D):
        kv = collections.defaultdict(int)
        for a in A:
            for b in B:
                kv[a + b] += 1
        result = 0
        for c in C:
            for d in D:
                if -(c + d) in kv:
                    result += kv[-(c + d)]
        return result

