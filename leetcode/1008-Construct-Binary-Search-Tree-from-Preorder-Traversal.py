class Solution(object):
    def bstFromPreorder(self, preorder):
        self.i = 0
        def buildBST(preorder, bound = float("inf")):
            if self.i == len(preorder) or preorder[self.i] > bound: return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = buildBST(preorder, root.val)
            root.right = buildBST(preorder, bound)
            return root
        return buildBST(preorder)
