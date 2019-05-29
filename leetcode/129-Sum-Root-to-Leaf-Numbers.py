class Solution:
    def sumNumbers(self, root):
        def _sum(root, total):
            if not root: return 0
            tmp = total * 10 + root.val
            if not root.left and not root.right: return tmp
            else: return _sum(root.left, tmp) + _sum(root.right, tmp)
        return _sum(root, 0)

