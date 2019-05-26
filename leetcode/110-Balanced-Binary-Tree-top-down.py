class Solution:
    def isBalanced(self, root):
        def _depth(root):
            if not root: return 0
            return max(_depth(root.left), _depth(root.right)) + 1
        if not root: return True
        left = _depth(root.left)
        right = _depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
