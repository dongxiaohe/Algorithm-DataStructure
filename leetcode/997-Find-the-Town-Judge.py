class Solution(object):
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for x, y in trust:
            count[x] -= 1
            count[y] += 1
        for i in range(1, len(count)):
            if count[i] == N - 1: return i
        return -1
