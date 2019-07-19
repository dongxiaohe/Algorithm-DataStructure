class Solution(object):
    def treeToDoublyList(self, root):
        if not root: return None
        def dfs(node):
            nonlocal first, last
            if node:
                if node.left: dfs(node.left)
                if not first:
                    first = last = node
                else:
                    last.right = node
                    node.left = last
                    last = last.right
                if node.right: dfs(node.right)
        first, last = None, None
        dfs(root)
        first.left = last
        last.right = first
        return first

