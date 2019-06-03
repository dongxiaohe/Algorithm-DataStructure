class Solution:
    def cloneGraph(self, node):
        if not node: return None
        root = Node(node.val, [])
        queue = collections.deque()
        nodeMap = collections.defaultdict(Node)
        nodeMap[node] = root
        queue.append(node)
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in nodeMap:
                    nodeMap[node].neighbors.append(nodeMap[neighbor])
                else:
                    neighborCopy = Node(neighbor.val, [])
                    nodeMap[neighbor] = neighborCopy
                    nodeMap[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
        return root
