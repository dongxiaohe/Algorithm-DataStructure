class Solution:
    def findRedundantConnection(self, edges):
        from collections import defaultdict
        graph = defaultdict(list)
        def _dfs_find(x, y, seen):
            if x not in seen: 
                seen.append(x)
                if x == y: return True
                return any([_dfs_find(rest, y, seen) for rest in graph[x]])
        for x, y in edges:
            if _dfs_find(x, y, []): return [x, y] 
            graph[x].append(y)
            graph[y].append(x)
