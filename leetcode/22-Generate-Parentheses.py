class Solution:
    def generateParenthesis(self, n):
        def _allValidPairs(maxOpened, opened, closed, s, result):
            if len(s) == maxOpened * 2:
                result.append(s)
                return
            if opened < maxOpened:
                _allValidPairs(maxOpened, opened + 1, closed, s + "(", result)
            if closed < opened:
                _allValidPairs(maxOpened, opened, closed + 1, s + ")", result)
        result = []
        _allValidPairs(n, 0, 0, "", result)
        return result
print(Solution().generateParenthesis(3))

