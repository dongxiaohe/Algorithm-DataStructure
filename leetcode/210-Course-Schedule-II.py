import collections
class Solution:
    def findOrder(self, n, pre):
        ind, dep = [0] * n, collections.defaultdict(list)
        for c, p in pre:
            ind[c] += 1
            dep[p].append(c)
        dq, result = collections.deque(), []
        for c in range(len(ind)):
            if ind[c] == 0: dq.append(c)
        while dq:
            tmp = dq.popleft()

            result.append(tmp)
            for t in dep[tmp]:
                ind[t] -= 1
                if ind[t] == 0: dq.append(t)
        return result if len(result) == n else []
print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

