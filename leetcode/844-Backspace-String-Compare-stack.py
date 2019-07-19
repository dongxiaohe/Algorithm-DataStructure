class Solution(object):
    def backspaceCompare(self, S, T):
        def build(_str):
            result = []
            for ch in _str:
                if ch != '#': result.append(ch)
                elif result: result.pop()
            return result
        return build(S) == build(T)
