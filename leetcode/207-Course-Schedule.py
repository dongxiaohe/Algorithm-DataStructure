import collections
class Solution:
    def canFinish(self, n, pre):
        ind, dep = collections.defaultdict(list), [0] * n
        for c, p in pre:
            dep[c] += 1
            ind[p].append(c)
        dq = collections.deque()
        for i in range(len(dep)):
            if dep[i] == 0: dq.append(i)
        k = 0
        while dq:
            tmp = dq.popleft()
            k += 1
            for t in ind[tmp]:
                dep[t] -= 1
                if dep[t] == 0: dq.append(t)
        return k == n

print(Solution().canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))

