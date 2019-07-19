class Solution(object):
    def isCousins(self, root, x, y):
        def dfs(node, parent, depth, value):
            if node:
                if node.val == value: return depth, parent
                return dfs(node.left, node, depth + 1, value) or dfs(node.right, node, depth + 1, value)
        xdep, xparent, ydep, yparent = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return xdep == ydep and xparent != yparent

