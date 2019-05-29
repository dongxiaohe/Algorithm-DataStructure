class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        if root.val == sum and not root.left and not root.right: return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

