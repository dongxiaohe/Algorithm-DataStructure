class Solution(object):
    def isValidBST(self, root):
        def _isValidBST(node, minVal, maxVal):
            if not node: return True
            if node.val <= minVal or node.val >= maxVal: return False 
            return _isValidBST(node.left, minVal, node.val) and _isValidBST(node.right, node.val, maxVal)
        return _isValidBST(root, float("-inf"), float("inf"))
