class Solution:
    def numDistinct(self, s, t):
        lenS, lenT = len(s), len(t)
        mem = [[0 for _ in range(lenS + 1)] for _ in range(lenT + 1)]
        for i in range(lenS): mem[0][i] = 1
        for i in range(lenT):
            for j in range(lenS):
                if s[j] == t[i]:
                    mem[i + 1][j + 1] = mem[i][j] + mem[i + 1][j]
                else:
                    mem[i + 1][j + 1] = mem[i + 1][j]
        return mem[lenT][lenS]

"""
We can use matrix (caching) to solve this problem. 

for example, s = abcabc t = ab

matrix would start with

1 1 1 1 1 1 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0

Note that: row is len(t) + 1 and column is len(s) + 1. The first entire row is 1 because of "" empty string

then we can build the matrix via two conditions:
1: if t[i] == s[j], mem[i + 1][j + 1] = mem[i + 1][j] + mem[i][j]
2: if t[i] != s[j], mem[i + 1][j + 1] = mem[i][j]

So the result would be:

1 1 1 1 1 1 1
0 1 1 1 2 2 2
0 0 1 1 1 3 3

"""