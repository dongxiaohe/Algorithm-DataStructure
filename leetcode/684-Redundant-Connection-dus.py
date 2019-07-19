class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self # this is to simplify find_assign_parent logic, otherwise node parameter can be the root node
        self.rank = 0

class Solution:
    def findRedundantConnection(self, edges):
        def make_node(nodes, node):
            if node in nodes: return nodes[node]
            nodes[node] = Node(node)
            return nodes[node]

        def find_assign_parent(node):
            if node.parent == node:  return node
            node.parent = find_assign_parent(node.parent)
            return node.parent
      
        def union(node1, node2): 
            parent1, parent2 = find_assign_parent(node1), find_assign_parent(node2)
            if parent1 == parent2: return False
            if parent1.rank == parent2.rank:
                parent1.rank += 1
                parent2.parent = parent1
            elif parent1.rank > parent2.rank:
                parent2.parent = parent1
            else:
                parent1.parent = parent2
            return True
        from collections import defaultdict
        nodes = defaultdict(Node)
        for x, y in edges:
            node1, node2 = make_node(nodes, x), make_node(nodes, y)
            if not union(node1, node2): return [x, y]
       
        
print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))
print(Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
