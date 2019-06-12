class Solution(object):
    def repeatedSubstringPattern(self, s):
        S = (s + s)[1: -1]
        return S.find(s) != -1

