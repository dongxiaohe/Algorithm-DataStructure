class Solution:
    def pruneTree(self, root):
        if not root: return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if not root.val and not root.left and not root.right: return None
        return root
