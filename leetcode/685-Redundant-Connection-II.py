class Solution:
    def findRedundantDirectedConnection(self, edges):
        parents, routes, sizes = {}, [0] * (len(edges) + 1), [0] * (len(edges) + 1)
        # step 1 find node has two parents
        ans1 = []
        ans2 = []
        def find(node):
            while routes[node] != node:
                routes[node] = routes[routes[node]]
                node = routes[node]
            return node
        for edge in edges:
            u, v = edge
            if v in parents and parents[v] > 0:
                ans1 = [parents[v], v]
                ans2 = [u, v]
                edge[0], edge[1] = -1, -1
            else:
                parents[v] = u
        for u, v in edges:
            if u < 0: continue
            if routes[u] == 0: routes[u] = u
            if routes[v] == 0: routes[v] = v
            pu, pv = find(u), find(v)
            if pu == pv: return ans1 if ans1 else [u, v]
            if sizes[pv] > sizes[pu]: pu, pv = pv, pu
            routes[pv] = pu
            sizes[pu] += sizes[pv]
        return ans2

