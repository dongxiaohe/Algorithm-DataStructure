class Solution:
    def buildTree(self, preorder, inorder):
        def _buildTree(preStart, inStart, inEnd, preorder, inorder, preEnd):
            if preStart > preEnd or inStart > inEnd: return None
            tmp = preorder[preStart]
            inPosition = inorder.index(tmp)
            root = TreeNode(tmp)
            root.left = _buildTree(preStart + 1, inStart, inPosition - 1, preorder, inorder, preEnd)
            root.right = _buildTree(preStart + inPosition - inStart + 1, inPosition + 1, inEnd, preorder, inorder, preEnd) # preStart + inPosition - inStart + 1 would find the right root
            return root
        end = len(inorder) - 1
        return _buildTree(0, 0, end, preorder, inorder, end)
