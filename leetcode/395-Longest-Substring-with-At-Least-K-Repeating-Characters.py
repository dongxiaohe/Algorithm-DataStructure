class Solution:
    def longestSubstring(self, s, k):
        result, h = 0, 1
        while h < 27:
            start, _max, unique, moreThanK, counts = 0, 0, 0, 0, [0] * 128
            i, n, start = 0, len(s), 0
            while i < n:
                index = ord(s[i])
                counts[index] += 1
                if counts[index] == 1: unique += 1
                if counts[index] == k: moreThanK += 1
                i += 1
                while unique > h:
                    counts[ord(s[start])] -= 1
                    if counts[ord(s[start])] == k - 1: moreThanK -= 1
                    if counts[ord(s[start])] == 0: unique -= 1
                    start += 1
                if moreThanK == unique: result = max(result, i - start)

            h += 1
        return result

