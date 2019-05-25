class Solution(object):
    def inorderTraversal(self, root):
        def _addResult(root, result):
            if root:
                if root.left: _addResult(root.left, result)
                result.append(root.val)
                if root.right: _addResult(root.right, result)
        result = []
        _addResult(root, result)
        return result
