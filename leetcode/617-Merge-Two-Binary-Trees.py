class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        value = 0
        if t1 and t2: value = t1.val + t2.val
        elif t1: value = t1.val
        else: value = t2.val
        node = TreeNode(value)
        node.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        node.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return node
