class Solution:
    def numDistinct(self, s, t):
        def _dfs(s, t, start, end, acc, result):
            if acc == t:
                result["counter"] += 1
                return
            for i in range(start, end):
                prefix = acc + s[i]
                if t.startswith(prefix):
                    _dfs(s, t, i + 1, end, prefix, result)
        result = {"counter": 0}
        _dfs(s, t, 0, len(s), "", result)
        return result["counter"]

# print(Solution().numDistinct("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
#                              "bddabdcae"))
print(Solution().numDistinct("abcabc", "ab"))