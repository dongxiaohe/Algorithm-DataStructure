class Solution(object):
    def countSubstrings(self, s):
        def countPal(s, l, r, result):
            while l >=0 and r < len(s) and s[l] == s[r]:
                result["count"] += 1
                l -= 1
                r += 1
        result = {"count": 0}
        for i in range(len(s)):
            countPal(s, i, i, result)
            countPal(s, i, i + 1, result)
        return result["count"]

