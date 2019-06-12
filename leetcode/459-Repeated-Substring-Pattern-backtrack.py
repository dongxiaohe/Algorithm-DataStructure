class Solution(object):
    def repeatedSubstringPattern(self, s):
        def dfs(s, start_index, pattern_size, acc):
            if start_index == len(s): return True
            if s[start_index: start_index + pattern_size] != acc: return False
            return dfs(s, start_index + len(acc), pattern_size, acc)
        for i in range(1, len(s)):
            if dfs(s, 0, i, s[:i]): return True
        return False
