import collections
def topologicalSort(graphs):
    visited, deque = collections.defaultdict(bool), collections.deque()
    for node in graphs:
        if visited[node]: continue
        dfs(node, visited, deque)
    return deque

def dfs(node, visited, deque):
    visited[node] = True
    for child in node.children:
        if visited[node]: continue
        dfs(child, visited, deque)
    deque.appendleft(node.val)

class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children

F = Node("F")
E = Node("E", [F])
C = Node("C", [E, F])
D = Node("D")
B = Node("B")
A = Node("A", [B, C])

def buildFromBottom(node):
    seen, deque = set(), collections.deque()
    def dfs(node, seen, deque):
        deque.appendleft(node.val)
        seen.add(node)
        for child in node.children:
            if child in seen: continue
            dfs(child, seen, deque)

    deque.appendleft(node.val)
    for eachNode in node.children:
        dfs(eachNode, seen, deque)

    return deque

def buildFromTop(node):
    seen, deque = set(), collections.deque()
    def dfs(node, seen, deque):
        seen.add(node)
        for child in node.children:
            if child in seen: continue
            dfs(child, seen, deque)
        deque.appendleft(node.val)

    for eachNode in node.children:
        dfs(eachNode, seen, deque)
    deque.appendleft(node.val)

    return deque

print(topologicalSort([F, E, C, D, B, A]), ["A", "B", "D", "C", "E", "F"])
print(buildFromBottom(A), ["F", "E", "C", "B", "A"])
print(buildFromTop(A), ["A", "C", "E", "F", "B"])

