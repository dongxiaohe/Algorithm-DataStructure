class Solution:
    def findDuplicates(self, nums):
        kv = collections.defaultdict(int)
        result = []
        for t in nums:
            if kv[t] == -1: result.append(t)
            else: kv[t] = -1
        return result
