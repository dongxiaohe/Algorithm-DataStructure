class Solution(object):
    def backspaceCompare(self, S, T):
        def eachCh(_str):
            skip = 0
            for ch in _str[::-1]:
                if ch == '#': skip += 1
                elif skip: skip -= 1
                else: yield ch
        return all(x == y for x, y in itertools.izip_longest(eachCh(S), eachCh(T)))
