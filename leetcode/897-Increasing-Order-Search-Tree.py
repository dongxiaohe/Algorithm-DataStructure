class Solution(object):
    def increasingBST(self, root):
        def transform(root, tail = None):
            if not root: return tail
            res = transform(root.left, root)
            root.left = None
            root.right = transform(root.right, tail)
            return res
        return transform(root)
