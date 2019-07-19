import collections
class Solution:
    def maxProduct(self, words):
        kv = collections.defaultdict(int)
        for word in words:
            key = 0
            for ch in set(word):
                key |= 1 << (ord(ch) - 97)
            kv[key] = max(kv[key], len(word))
        maxCount = 0
        for x in kv:
            for y in kv:
                if x & y == 0: 
                    maxCount = max(maxCount, kv[x] * kv[y])
        return maxCount
