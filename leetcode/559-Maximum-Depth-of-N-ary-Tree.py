class Solution(object):
    def maxDepth(self, root):
        def _maxDepth(node):
            if not node or not node.children: return 1
            return max(list(map(lambda x: 1 + _maxDepth(x), node.children)))
        if not root: return 0
        return _maxDepth(root)
