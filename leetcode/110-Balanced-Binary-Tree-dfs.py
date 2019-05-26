class Solution:
    def isBalanced(self, root):
        def _dfsHeight(root):
            if not root: return 0
            leftHeight = _dfsHeight(root.left)
            if leftHeight == -1: return -1
            rightHeight = _dfsHeight(root.right)
            if rightHeight == -1: return -1
            print(root.val)
            print(leftHeight, rightHeight) # Left and right are always start with 0 height and then traverse back to root node.
            if abs(leftHeight - rightHeight) > 1: return -1
            return max(leftHeight, rightHeight) + 1
        return _dfsHeight(root) != -1

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

node7 = TreeNode(45)
node6 = TreeNode(30, None, node7)
node4 = TreeNode(15, node6)
node5 = TreeNode(7)
node3 = TreeNode(20, node4, node5)
node2 = TreeNode(9)
node1 = TreeNode(3, node2, node3)

print(Solution().isBalanced(node1))

