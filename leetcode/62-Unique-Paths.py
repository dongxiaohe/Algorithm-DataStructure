class Solution:
    def uniquePaths(self, m, n):
        if m < n: return self.uniquePaths(n, m)
        cur = [1 for _ in range(m)]
        for _ in range(1, n):
            for j in range(1, m):
                cur[j] += cur[j - 1]
        return cur[m - 1]

print(Solution().uniquePaths(7, 3))

"""
def test(m, n):
    path = [ [1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            path[i][j] = path[i - 1][j] + path[i][j - 1]
    return path[m - 1][n - 1]

def test2(m, n):
    if m > n: return test2(n, m)
    pre = [1 for _ in range(m)]
    cur = [1 for _ in range(m)]
    for i in range(1, n):
        for j in range(1, m):
            cur[j] = cur[j - 1] + pre[j]
        cur, pre = pre, cur
    return pre[m - 1]
"""