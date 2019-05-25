class Solution:
    def isInterleave(self, s1, s2, s3):
        def _dfs(s1, s2, s3, i, j, k, lenS1, lenS2, lenS3, invalid):
            if k == lenS3: return True
            if invalid[i][j]: return False
            isValid = j < lenS2 and s2[j] == s3[k] and _dfs(s1, s2, s3, i, j + 1, k + 1, lenS1, lenS2, lenS3, invalid) or i < lenS1 and s1[i] == s3[k] and _dfs(s1, s2, s3, i + 1, j, k + 1, lenS1, lenS2, lenS3, invalid)
            if not isValid: invalid[i][j] = True
            return isValid
        lenS1, lenS2, lenS3 = len(s1), len(s2), len(s3)
        if lenS1 + lenS2 != lenS3: return False
        invalid = [[False for _ in range(lenS2 + 1)] for _ in range(lenS1 + 1)]
        return _dfs(s1, s2, s3, 0, 0, 0, lenS1, lenS2, lenS3, invalid)

# print(Solution().isInterleave("", "abc", "abc"))
# print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))
# print(Solution().isInterleave("bcaccccacccaa", "aabccbbbbbaca", "aabcbccbbbabaaccccacacccba"))
# print(Solution().isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
#                               "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
#                               "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
