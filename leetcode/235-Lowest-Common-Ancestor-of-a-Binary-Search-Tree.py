class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val: return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val and root.val <= q.val: return root
        elif root.val < p.val: return self.lowestCommonAncestor(root.right, p, q)
        else: return self.lowestCommonAncestor(root.left, p, q)
