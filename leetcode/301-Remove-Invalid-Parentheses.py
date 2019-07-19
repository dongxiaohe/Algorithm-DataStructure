class Solution(object):
    def removeInvalidParentheses(self, s):
        left = right = 0
        for ch in s:
            if ch == "(": left += 1
            elif ch == ")":
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else 0
        def backtrack(s, index, left, right, opened, acc, result):
            if index == len(s):
                if opened == left == right == 0:
                    result[acc] = 1
                return
            if (s[index] == "(" and left > 0) or (s[index] == ")" and right > 0):
                backtrack(s, index + 1, left - (s[index] == "("), right - (s[index] == ")"), opened, acc, result)
            if s[index] != "(" and s[index] != ")":
                backtrack(s, index + 1, left, right, opened, acc + s[index], result)
            elif s[index] == "(":
                backtrack(s, index + 1, left, right, opened + 1, acc + s[index], result)
            elif s[index] == ")" and opened > 0:
                backtrack(s, index + 1, left, right, opened - 1, acc + s[index], result)
        result = {}
        backtrack(s, 0, left, right, 0, "", result)
        return list(result.keys())

