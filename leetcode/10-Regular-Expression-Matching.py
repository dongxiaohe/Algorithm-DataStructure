class Solution(object):
    def isMatch(self, s, p):
        matrix = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        matrix[0][0] = True
        for j in range(len(p)):
            if p[j] == "*" and matrix[0][j - 1]: matrix[0][j + 1] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == ".":
                    matrix[i + 1][j + 1] = matrix[i][j]
                elif p[j] == "*":
                    if j > 0 and s[i] != p[j - 1] and p[j - 1] != ".":
                        matrix[i + 1][j + 1] = matrix[i + 1][j - 1]
                    else:
                        matrix[i + 1][j + 1] = matrix[i][j + 1] or matrix[i + 1][j] or matrix[i + 1][j - 1]
        return matrix[len(s)][len(p)]
