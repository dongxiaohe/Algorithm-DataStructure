class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return left + right + 1 if left == 0 or right == 0 else min(left, right) + 1# The reason for left == 0 or right == 0 is tree can be the linked list for the extreme scenario
