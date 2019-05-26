class Solution:
    def buildTree(self, inorder, postorder):
        def _buildTree(postStart, postEnd, inStart, inEnd, inorder, postorder):
            if postStart > postEnd or inStart > inEnd: return None
            tmp = postorder[postEnd]
            inPosition = inorder.index(tmp)
            root = TreeNode(tmp)
            root.left = _buildTree(postStart, postStart + inPosition - inStart - 1, inStart, inPosition - 1, inorder, postorder) # postEnd actually depends on postStart
            root.right = _buildTree(postStart + inPosition - inStart, postEnd - 1, inPosition + 1, inEnd, inorder, postorder) # poStart actually depends on inPosition
            return root
        end = len(postorder) - 1
        return _buildTree(0, end, 0, end, inorder, postorder)
