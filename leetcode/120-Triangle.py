class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        m = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                m[j] = min(m[j], m[j + 1]) + triangle[i][j]
        return m[0]

tmp = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution().minimumTotal(tmp))

"""
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
  
This is the optimization problem. In another word, this is a dp problem. If we use one dimension array to record the state, then m[i] = min(m[i] + m[i + 1]) + triangle[i][j]

[4,1,8,3,0]
[7,6,10,3,0]
[9,10,10,3,0]
[11,10,10,3,0]

so m[0] is the one we are looking for.
"""