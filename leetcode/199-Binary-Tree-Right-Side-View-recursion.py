class Solution(object):
    def rightSideView(self, root):
        def _rightSideView(root, result, depth):
            if not root: return
            if depth == len(result):
                result.append(root.val)
            _rightSideView(root.right, result, depth + 1)
            _rightSideView(root.left, result, depth + 1)
        result = []
        _rightSideView(root, result, 0)
        return result
