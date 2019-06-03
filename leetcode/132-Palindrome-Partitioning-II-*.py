class Solution:
    def minCut(self, s):
        cuts, n = [], len(s)
        for i in range(n + 1): cuts.append(i - 1)
        for i in range(n):
            j = 0
            while j <= i and i + j < n and s[i - j] == s[i + j]:
                cuts[i + j + 1] = min(cuts[i + j + 1], 1 + cuts[i - j])
                j += 1
            j = 1
            while j <= i + 1 and i + j < n and s[i - j + 1] == s[i + j]:
                cuts[i + j + 1] = min(cuts[i + j + 1], 1 + cuts[i -j + 1])
                j += 1
        return cuts[n]

