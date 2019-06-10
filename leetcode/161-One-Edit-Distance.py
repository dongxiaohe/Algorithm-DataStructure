class Solution(object):
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m > n: return self.isOneEditDistance(t, s)

        if m - n > 1: return False
        for i in range(m):
            if s[i] != t[i]:
                if m != n: return s[i:] == t[i + 1:]
                else: return s[i + 1:] == t[i + 1:]
        return m + 1 == n
