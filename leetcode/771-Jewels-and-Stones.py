class Solution(object):
    def numJewelsInStones(self, J, S):
        kv = collections.defaultdict(int)
        for ch in S: kv[ch] += 1
        result = 0
        for ch in J: result += kv[ch]
        return result
