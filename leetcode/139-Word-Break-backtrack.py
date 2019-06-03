class Solution:
    def wordBreak(self, s, wordDict):
        def _wordBreak(s, words, mem):
            if s in mem: return mem[s]
            res = False
            if len(s) == 0:
                mem["isFound"] = True
                return True
            for word in words:
                if s.startswith(word):
                    res = _wordBreak(s[len(word):], words, mem)
            mem[s] = res
            return res
        mem = {
            "isFound": False
        }
        _wordBreak(s, wordDict, mem)

        return mem["isFound"]
