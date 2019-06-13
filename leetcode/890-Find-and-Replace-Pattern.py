class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(word, pattern):
                if P.setdefault(x, y) != y: return False
            return len(set(P.values())) == len(P.values()) # remove different characters match to same character
        return filter(match, words)

