class Solution:
    def countNodes(self, root):
        def height(node):
            if not node: return 0
            return height(node.left) + 1
        def lastLevelNodes(node, level, h):
            if not node: return 0
            if level == h: return 1
            return lastLevelNodes(node.left, level + 1, h) + lastLevelNodes(node.right, level + 1, h)
        h = height(root)
        if h == 0: return 0
        return (1 << (h - 1)) - 1 + lastLevelNodes(root, 1, h)

