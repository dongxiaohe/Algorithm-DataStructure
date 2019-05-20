class DSU:
    def __init__(self, n):
        self.parent = range(1000)
        self.count = n
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]
    def union(self, node1, node2):
        self.parent[self.find(node1)] = self.find[node2]
        self.count -= 1

class Solution(object):
    def removeStones(self, stones):
        dsu = DSU(len(stones()))
        for x, y in stones:
            dsu.union(x, y)
        return dsu.count


