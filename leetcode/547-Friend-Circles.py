class DisjointSet:
    def __init__(self, n):
        self.count = n
        self.sizes = collections.defaultdict(int)
        self.parent = list(range(n)) # treat list as a map, since friend is marked as a number
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            if self.sizes[parent1] < self.sizes[parent2]: parent1, parent2 = parent2, parent1 
            self.sizes[parent1] += self.sizes[parent2]
            self.parent[parent2] = parent1
            self.count -= 1
class Solution:
    def findCircleNum(self, M):
        numFriend = len(M)
        disjointSet = DisjointSet(numFriend)
        for i in range(numFriend):
            for j in range(i + 1, numFriend):
                if M[i][j] == 1: disjointSet.union(i, j)
        return disjointSet.count
