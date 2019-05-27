class Node:
    def __init__(self, val, children = None):
        self.val = val
        self.children = children
    #if it is a graph, we need to set visited attribute to avoid duplication

node100 = Node(100)
node7 = Node(7)
node6 = Node(6, [node7])
node5 = Node(5, [node6])
node4 = Node(4)
node3 = Node(3, [node4, node5])
node2 = Node(2)
node1 = Node(1, [node2, node3, node100]) 

def bfs(root):
    if not root: return []
    stack, result = [root], []
    while stack:
        tmp = stack.pop(0)
        result.append(tmp.val)
        if tmp.children: stack.extend(tmp.children)
    return result

print(bfs(node1))

def dfs(root):
    if not root: return []
    stack, result = [root], []
    while stack:
        tmp = stack.pop()
        result.append(tmp.val)
        if tmp.children: stack.extend(tmp.children)
    return result

print(dfs(node1))