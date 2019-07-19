class Solution(object):
    def isBipartite(self, graph):
        colorNode = collections.defaultdict(int)
        for index in range(len(graph)):
            if index not in colorNode:
                colorNode[index] = 0
                stack = [index]
                while stack:
                    nodeIndex = stack.pop()
                    for neigh in graph[nodeIndex]:
                        if neigh in colorNode and colorNode[neigh] == colorNode[nodeIndex]: return False
                        elif neigh not in colorNode:
                            stack.append(neigh)
                            colorNode[neigh] = colorNode[nodeIndex] ^ 1
        return True
