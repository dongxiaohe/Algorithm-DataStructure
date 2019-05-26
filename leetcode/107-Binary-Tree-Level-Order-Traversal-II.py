class Solution:
    def levelOrderBottom(self, root):
        def _buildList(root, result, level):
            if not root: return
            if len(result) < level + 1:
                result.insert(0, [])
            _buildList(root.left, result, level + 1)
            _buildList(root.right, result, level + 1)
            result[len(result) - level - 1].append(root.val)
        result = []
        _buildList(root, result, 0)
        return result

