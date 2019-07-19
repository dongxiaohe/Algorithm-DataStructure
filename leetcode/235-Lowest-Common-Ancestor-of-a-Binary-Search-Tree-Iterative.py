class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        This is a great trick to check:
            1. if root is equal to p or q, jump out of the while loop
            2. if root is not in range, jump out of the while loop
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
        return root
