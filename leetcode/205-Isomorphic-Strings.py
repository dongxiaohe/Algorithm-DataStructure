class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False
        map1, map2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(s)):
            if map1[s[i]] != map2[t[i]]: return False
            map1[s[i]] = i + 1
            map2[t[i]] = i + 1
        return True
