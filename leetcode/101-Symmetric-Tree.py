class Solution:
    def isSymmetric(self, root):
        if not root: return True
        def _isMirror(left, right):
            if not left and not right: return True
            if left and right: return left.val == right.val and _isMirror(left.left, right.right) and _isMirror(left.right, right.left)
            else: return False
        return _isMirror(root.left, root.right)
                
