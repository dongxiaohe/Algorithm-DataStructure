class Solution:
    def longestValidParentheses(self, s):
        if not s: return 0
        match = [0] * len(s)
        for i in range(len(s)):
            if s[i] == "(": continue
            start = i - 1 - match[i - 1]
            if start < 0 or s[start] != "(": continue
            match[i] = match[start - 1] + i - start + 1
        return max(match)
