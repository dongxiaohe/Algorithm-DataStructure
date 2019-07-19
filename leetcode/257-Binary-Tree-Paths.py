class Solution(object):
    def binaryTreePaths(self, root):
        def _buildPath(root, path, result):
            if not root.left and not root.right: result.append(path + str(root.val))
            if root.left: _buildPath(root.left, path + str(root.val) + "->", result)
            if root.right: _buildPath(root.right, path + str(root.val) + "->", result)
        result = []
        if root: _buildPath(root, "", result)
        return result
