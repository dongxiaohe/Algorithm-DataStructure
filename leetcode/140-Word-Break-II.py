class Solution:
    def wordBreak(self, s, wordDict):
        def _dfs(s, words, mem):
            if s in mem: return mem[s]
            res = []
            if len(s) == 0:
                res.append("")
                return res
            for word in words:
                if s.startswith(word):
                    sublist = _dfs(s[len(word):], words, mem)
                    for each in sublist:
                        if each == "": res.append(word)
                        else: res.append(word + " " + each)
            mem[s] = res
            return res
        return _dfs(s, wordDict, { })
